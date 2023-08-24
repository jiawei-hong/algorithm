import sys

for text in sys.stdin.readlines():
    text = text.strip()
    s = []

    for i in range(len(text)-1):
        s.append(str(abs(ord(text[i]) - ord(text[i+1]))))

    print(''.join(s))
