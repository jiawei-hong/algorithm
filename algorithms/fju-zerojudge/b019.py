n = int(input())

for _ in range(n):
    a, b, c, s = map(int, input().split())
    total = s + 20
    b_c_sum = b + c
    diff = (total - b_c_sum) // 3
    hua = c + diff
    qiqi = b + diff
    lai = total - hua - qiqi

    print(' '.join(map(str, [c+diff, b+diff, lai])))
