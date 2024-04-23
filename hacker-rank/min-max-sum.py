#!/bin/python3

import math

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    min_num = math.inf
    max_num = -(math.inf)
    n = len(arr)

    for i in range(n):
        tmp_num = 0
        for j in range(n):
            if i != j:
                tmp_num += arr[j]
        min_num = min(tmp_num, min_num)
        max_num = max(tmp_num, max_num)
    print(min_num, max_num)


if __name__ == "__main__":

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
