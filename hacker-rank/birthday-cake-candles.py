#!/bin/python3

import math
import os
from collections import defaultdict

#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#


def birthdayCakeCandles(candles):
    # Write your code here
    max_num = -(math.inf)
    res = defaultdict(int)

    for candle in candles:
        res[candle] += 1
        max_num = max(candle, max_num)

    return res[max_num]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + "\n")

    fptr.close()
