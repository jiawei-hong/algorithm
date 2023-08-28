n = int(input())

fib = [0,1]

for i in range(2,151):
    fib.append(fib[i-1]+fib[i-2])

for _ in range(n):
    num = int(input())
    print(str(sum(map(lambda x: x **2 ,fib[:num+1]))))
