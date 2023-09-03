n = int(input())

for _ in range(n):
    s = input()

    while len(s) > 1:
        s = str(sum(map(int, list(s))))

    print(s)
