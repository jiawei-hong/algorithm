n = int(input())

for _ in range(n):
    t, s = input().split()
    t = int(t)
    res = []

    for i in range(len(s)):
        decode_num = ord(s[i]) - t

        if decode_num < 65:
            decode_num = 91 - (65-decode_num)
        res.append(chr(decode_num))

    print(''.join(res))
