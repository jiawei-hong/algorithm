n = int(input())


for _ in range(n):
    num = int(input())
    bin_num = bin(num)
    cnt = bin_num.count('1')
    res = 'YES' if cnt % 2 == 1 else 'NO'
    print(f'{num}: {res}')
