def sum_two_array(a, b):
    res = [0] * len(a)

    for i in range(len(a)):
        res[i] += int(a[i])+int(b[i])

    return res


n = int(input())

for _ in range(n):
    a, b = map(list, input().split())
    diff = abs(len(a) - len(b))

    if len(a) > len(b):
        b = [0] * diff + b
    elif len(b) > len(a):
        a = [0] * diff + a

    res = sum_two_array(a, b)
    ans = list(filter(lambda x: x > 9, res))

    print(str(len(ans)))
