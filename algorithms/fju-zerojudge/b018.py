n = int(input())

for _ in range(n):
    isbn = input()
    nums = enumerate(list(isbn.replace('-', '')))
    sum  = 0

    for i, num in nums:
        sum += int(num) if i % 2 == 0 else int(num) * 3
    
    diff = 10 - (sum % 10)
    res = 0 if diff == 10 else diff

    print(f'ISBN {isbn}-{res}')
