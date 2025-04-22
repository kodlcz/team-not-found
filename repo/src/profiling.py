from calc_lib import *
import sys
nums = []
numCount = 0
count = 0
for val in sys.stdin.read().split():
    try:
        nums.append(float(val))
        numCount = add(numCount,val)
        count = add(count,1)
    except ValueError:
        print("zadané špatné číslo: ", val)
prum = div(numCount,count)
rozdil = 0
for i in nums:
    rozdil =  add(rozdil,expon(sub(i,prum),2))
print(sqr(div(rozdil,sub(count,1)),2))

