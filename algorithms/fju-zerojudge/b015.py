n = int(input())


def f(s):
    n = len(s)
    return (s[1:n] + s[0]).upper() + 'AY'


for _ in range(n):
    data = map(f, input().split())

    print(' '.join(data))
