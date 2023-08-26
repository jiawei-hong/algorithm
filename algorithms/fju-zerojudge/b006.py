n = int(input())

for _ in range(n):
    raw = input()

    set_raw = set(raw)

    if len(set_raw) != 2:
        print('No')
    elif raw[0] == raw[1] or raw[1] == raw[2] or raw[2] == raw[3]: 
        print('No')
    else:
        print('Yes')
