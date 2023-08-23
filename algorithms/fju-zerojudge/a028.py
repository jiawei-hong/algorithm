n = int(input())

for i in range(n):
    y = int(input())
    if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
        print(f"Case {i+1}: a leap year")
    else:
        print(f"Case {i+1}: a normal year")
