
<h1 align="center">Git DeLorean</h3>

# About The Project

A way to rewrite (git) history by going back a certain number of commits, making a change and restoring the rest.

# Usage
```
usage: gitdelorean [-h] [-c COMMITS] {back,restore}

positional arguments:
  {back,restore}        Either go back a certain number of commits or restore the commits you went back on

options:
  -h, --help            show this help message and exit
  -c COMMITS, --commits COMMITS
                        Number of commits to go back
```

### Going back a certain number of commits

```
kjnix@arch % python3 gitdelorean.py back -c 10
```

Results:
```
Stashing: 'feat(file_10.txt): commit #10'
Stashing: 'feat(file_9.txt): commit #9'
Stashing: 'feat(file_8.txt): commit #8'
Stashing: 'feat(file_7.txt): commit #7'
Stashing: 'feat(file_6.txt): commit #6'
Stashing: 'feat(file_5.txt): commit #5'
Stashing: 'feat(file_4.txt): commit #4'
Stashing: 'feat(file_3.txt): commit #3'
Stashing: 'feat(file_2.txt): commit #2'
Stashing: 'feat(file_1.txt): commit #1'
```

### Restoring the commits you went back on

```
kjnix@arch % python3 gitdelorean.py back -c 10
```

Results:
```
Restoring: 'feat(file_1.txt): commit #1'
Restoring: 'feat(file_2.txt): commit #2'
Restoring: 'feat(file_3.txt): commit #3'
Restoring: 'feat(file_4.txt): commit #4'
Restoring: 'feat(file_5.txt): commit #5'
Restoring: 'feat(file_6.txt): commit #6'
Restoring: 'feat(file_7.txt): commit #7'
Restoring: 'feat(file_8.txt): commit #8'
Restoring: 'feat(file_9.txt): commit #9'
Restoring: 'feat(file_10.txt): commit #10'
```

