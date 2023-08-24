import sys

record = {
    "A": "10",
    "N": "22",
    "B": "11",
    "O": "35",
    "C": "12",
    "P": "23",
    "D": "13",
    "Q": "24",
    "E": "14",
    "R": "25",
    "F": "15",
    "S": "26",
    "G": "16",
    "T": "27",
    "H": "17",
    "U": "28",
    "I": "34",
    "V": "29",
    "J": "18",
    "W": "32",
    "K": "19",
    "X": "30",
    "L": "20",
    "Y": "31",
    "M": "21",
    "Z": "33",
}

for line in sys.stdin.readlines():
    r = []
    line = line.strip()
    checkPoint = (10 - int(line[-1])) % 10
    x = 0

    for i in range(8):
        x += int(line[i])*(8-i)

    for k, v in record.items():
        eng = int(v[0]) + (int(v[1]) * 9)

        if (eng+x) % 10 == checkPoint:
            r.append(k)

    r = sorted(r)

    print(''.join(r))
