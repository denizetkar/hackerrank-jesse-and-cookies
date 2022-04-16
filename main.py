#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#
from collections import deque


def smallest_of(q1, q2):
    smallest, q = None, None
    if len(q1) > 0:
        smallest = q1[0]
        q = q1
    if len(q2) > 0:
        if smallest is None or q2[0] < smallest:
            smallest = q2[0]
            q = q2
    if q is not None:
        q.popleft()
    return smallest


def cookies(k, A):
    A.sort()
    q1 = deque(A)
    q2 = deque()

    cnt = 0
    while True:
        smallest = smallest_of(q1, q2)
        if smallest >= k:
            break
        next_smallest = smallest_of(q1, q2)
        if next_smallest is None:
            return -1
        q2.append(smallest + 2 * next_smallest)
        cnt += 1
    return cnt


if __name__ == "__main__":
    with open(os.environ["INPUT_PATH"], "r") as f, open(os.environ["OUTPUT_PATH"], "w") as fptr:

        first_multiple_input = f.readline().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, f.readline().rstrip().split()))

        result = cookies(k, A)

        fptr.write(str(result) + "\n")
