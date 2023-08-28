n = int(input())

for i in range(n):
    nums = list(map(int, input().split()))
    record = []
    b = True

    for num in nums:

        if num in record or num > 49:
            b = False
            break

        record.append(num)

    print('Yes' if b else 'No')
    
