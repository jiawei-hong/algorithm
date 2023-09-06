
def compute_sum(m, n):
    return sum([(i * m + 1) for i in range(n + 1)])


n = int(input())

for _ in range(n):
    m, mx = map(int, input().split())
    n = 0

    while compute_sum(m, n) <= mx:
        n += 1

    last_term = (n-1) * m + 1
    print(last_term)
