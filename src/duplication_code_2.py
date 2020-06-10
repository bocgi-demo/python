import os
import sys

def terrible_duplication2(i, j):
    if i > 100:
        if i % 3 < 2:
            for j in range(i):
                x = int(str(j) + str(i))
                if x % 2:
                    break
            else:
                x = 0
        else:
            for k in range(x):
                x += k
    return x


def terrible_duplication(i, j):
    if i > 100:
        if i % 3 < 2:
            for j in range(i):
                x = int(str(j) + str(i))
                if x % 2:
                    break
            else:
                x = 0
        else:
            for k in range(x):
                x += k
    return x