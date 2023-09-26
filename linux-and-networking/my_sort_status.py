import sys

lines = sys.stdin.readlines()
sorted_lines = sorted(lines, reverse=True)
for line in sorted_lines:
    sys.stderr.write(line)
