from collections import Counter

n = int(input())

for _ in range(n):
    counter = Counter(input().split())
    most_common = counter.most_common()
    mx_num = most_common[0][1]
    find_mx_num_in_the_most_common = list(filter(
        lambda x: x[1] == mx_num, most_common))

    for k, v in find_mx_num_in_the_most_common:
        print(f'{k},{v}')
