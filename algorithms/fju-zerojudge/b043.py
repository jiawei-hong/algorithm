import sys

for line in sys.stdin.readlines():
    num = int(line)

    if num == 0:
        break

    while len(str(num)) > 1:
        num = sum(map(int, list(str(num))))

    print(str(num))
