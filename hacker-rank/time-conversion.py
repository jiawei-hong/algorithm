#!/bin/python3

import os

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    s = s.split(":")
    in_night = "PM" in s[-1]
    s[-1] = s[-1][:2]

    if s[0] == "12":
        s[0] = "12" if in_night else "00"
    elif in_night:
        s[0] = str(int(s[0]) + 12)

    return ":".join(s)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    s = input()

    result = timeConversion(s)

    fptr.write(result + "\n")

    fptr.close()
