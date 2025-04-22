from calc_lib import *
import sys
num = []
numCount = 0
count = 0
for val in sys.stdin.read().split():
    try:
        num.append(float(val))
        numCount += val
        count += 1
    except ValueError:
        print("zadané špatné číslo: ", val)

