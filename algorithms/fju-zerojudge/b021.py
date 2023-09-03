n = int(input())

for _ in range(n):
    total, back_count = map(int ,input().split())
    back_people = list(map(int, input().split()))

    if total == back_count:
        print('*') 
    else:
        res = []

        for i in range(1, total+1):
            if i not in back_people:
                res.append(i)

        print(' '.join(map(str, res)) + ' ')

