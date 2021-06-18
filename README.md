## What it does

    > cd /path/to/interesting/git/repo
    > python /path/to/git_log_barchart/commit_times.py
    hour count commits
    0    19    |||||||||||||||||||
    1    13    |||||||||||||
    2    2     ||
    8    2     ||
    9    8     ||||||||
    10   3     |||
    11   2     ||
    12   15    |||||||||||||||
    13   1     |
    14   6     ||||||
    15   13    |||||||||||||
    16   6     ||||||
    17   23    |||||||||||||||||||||||
    18   21    |||||||||||||||||||||
    19   25    |||||||||||||||||||||||||
    20   29    |||||||||||||||||||||||||||||
    21   23    |||||||||||||||||||||||
    22   26    ||||||||||||||||||||||||||
    23   32    ||||||||||||||||||||||||||||||||
    total_commits: 269


## Features

Besides printing a barchart like shown above you can add arguments which will be passed to git log to filter which commits you wish to inspect.

To only look at your commits after a date:

    python commit_times.py --author=your.email@domain.com --since=2021-05

To only look at commits in a specific folder

    python commit_times.py -- path/to/file/or/folder


## Known issues

--author="Your Name" does not work, use --author=your.email@domain.com instead.