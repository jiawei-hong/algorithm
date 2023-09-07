
def f(name):
    return (len(name), name)


k = int(input())
names = []

for _ in range(k):
    name = input()
    names.append(name)

sorted_names = sorted(names, key=f)

for name in sorted_names:
    print(name)
