n = int(input())

for _ in range(n):
    num, s = input().split()
    res = ''
    groupCount = len(s) // int(num)

    for i in range(0, len(s), groupCount):
        res += ''.join(reversed(s[i:i+groupCount]))

    print(res)
