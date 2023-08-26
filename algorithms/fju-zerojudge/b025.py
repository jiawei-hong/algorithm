import sys

for line in sys.stdin.readlines():
    raw = int(line)

    if raw == 0:
        break

    money = [50, 10, 5 ,1]
    res = []

    for m in money:
        cnt = raw // m
        raw -= cnt * m
        res.append(str(cnt))

    print(' '.join(res))
