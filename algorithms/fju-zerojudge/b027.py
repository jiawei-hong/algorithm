n = int(input())

for _ in range(n):
    s = list(map(lambda x: str(int(not x)), list(map(int, input()))))

    print(''.join(s))
