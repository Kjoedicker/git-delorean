import argparse
import subprocess
import re
import sys

class Terminal:
    def run(command: str) -> str:
        results = subprocess.run(command, shell=True, capture_output=True)
        if (results.returncode != 0):
            sys.exit(f"[ERROR] executing command: '{command}'")
        return results.stdout.decode().strip().strip()

class Git:
    def getHeadCommitMessage():
        command = "git log -1 --pretty='%s'"
        return Terminal.run(command)
    
    def getHeadStashMessage():
        command = "git stash list -1 --pretty='%s'"
        return Terminal.run(command)

    def stash(message: str):
        command = f"git stash push -m '{message}' --include-untracked"
        Terminal.run(command)

    def reset():
        command = 'git reset --soft head~1'
        Terminal.run(command)

    def popStash():
        command = 'git stash pop'
        Terminal.run(command)

    def addAll():
        command = "git add ."
        Terminal.run(command)
    
    def commit(message: str):
        command = f"git commit -m '{message}' --no-verify"
        Terminal.run(command)

class GitDeLorean:
    def __init__(self):
        self.delimiter = "git-delorean-stash "

    def resetAndStash(self, totalCommits: int):
        for _ in range(1, totalCommits + 1):
            message = Git.getHeadCommitMessage()
            formattedMessage = self.delimiter+message
            
            print(f"Stashing: '{message}'")
            Git.reset()
            Git.stash(formattedMessage)

    def parseStashMessage(self, message):
        return re.compile(":\s?(.*)").split(message)[1].split(self.delimiter)[1]

    def restoreStashedCommits(self):
        message = Git.getHeadStashMessage()

        try:
            parsedMessage = self.parseStashMessage(message)
        # `IndexError` indicates the delimiter matched.
        # Which means there are no more related stashes to restore.
        except IndexError:
            return False

        print(f"Restoring: '{parsedMessage}'")
        Git.popStash()
        Git.addAll()
        Git.commit(parsedMessage)

        self.restoreStashedCommits()

class Cli:
    parser = argparse.ArgumentParser(
        prog='Git-DeLorean'
    )

    parser.add_argument("action", choices=["back", "restore"])
    parser.add_argument('-c', '--commits', type=int, help="Number of commits to go back")

    def getArguments(self):
        return self.parser.parse_args()

if __name__ == '__main__':
    args = Cli().getArguments()
    gitDeLorean = GitDeLorean()

    match (args.action):
        case "back":
            if not args.commits:
                sys.exit("Total number of commits must be specified")
            gitDeLorean.resetAndStash(args.commits)
        case "restore":
            gitDeLorean.restoreStashedCommits()