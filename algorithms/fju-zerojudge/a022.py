[h, m] = list(map(int, input().split()))

total_m = h * 60 + m

if total_m >= 450 and total_m < 1020:
    print("At School")
else:
    print("Off School")
