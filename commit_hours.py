from collections import defaultdict
import sys
import subprocess

if '-h' in sys.argv or '--help' in sys.argv:
    print('Prints which hours of the day commits in all branch have been made in this repo.')
    print("All arguments will be piped to git log, so see git log --help for more details.")
    print()
    print("Example:")
    print(" python commit_times.py --author=your.email@domain.com --since=2021-05")
    print(" python commit_times.py --author=your.email@domain.com -- path/to/file/or/folder")
    print()
    print("Known issues:")
    print('Dont use --author="your name", the string will not be properly handled (it will be treated as seperate arguments), use the email instead.')
    # TODO what about timezones?
    exit(0)

args_to_git = " ".join(sys.argv[1:])
git_command = f"git log --all --pretty='%ad' --date=format:'%H:%M:%S' {args_to_git}"
result = subprocess.run(git_command, capture_output=True, text=True)
lines = result.stdout.strip().splitlines()
if not lines:
    print(f"Tried to run: {git_command} but got no commits")
    if result.stderr:
        print("stderr:", result.stderr)
    exit(1)
lines = [line.replace("'", "") for line in lines]

commit_hours = defaultdict(list)

for line in lines:
    if line == "":
        continue
    hour, minute, second = map(int,line.split(":"))
    commit_hours[hour].append((hour,minute,second))

largest_count = max(len(values) for values in commit_hours.values())

def char_bar(count, max_width=80, largest_count=largest_count):
    width = count
    if largest_count > max_width:
        # All lengths must be a percentage of max_width instead.
        percent = count / largest_count
        width = round(percent * max_width)

    # Ensure that no bars exist only for 0 commits
    if count > 0:
        width = max(width, 1)

    return '|'*width


count_column_width = max(len(str(largest_count)), len('count'))
line_format = f"{{0:<5}}{{1:<{count_column_width}}} {{2}}"
print(line_format.format('hour', 'count', 'commits'))

for h in range(0, 24):
    count = len(commit_hours[h])
    # if count == 0:
    #     continue
    print(line_format.format(h, count, char_bar(count)))

total_commits = sum(len(v) for k, v in commit_hours.items())
print('total_commits:', total_commits)