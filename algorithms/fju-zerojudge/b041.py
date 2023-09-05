def f(ss):
    s = set()

    for i in range(len(ss) - 1):
        cur = ss[i:i+2]
        s.add(cur)

    return len(s)


k = int(input())

for _ in range(k):
    input_string = input()
    print(f(input_string))
