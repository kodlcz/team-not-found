from calc_lib import *
import sys
"""
@file profiling.py
@author Adam Kadlec
@brief Výpočet výběrové směrodatné odchylky ze standardního vstupu pomocí vlastní matematické knihovny.
@details Program načítá čísla ze standardního vstupu, vypočítá aritmetický průměr a následně výběrovou směrodatnou odchylku.
"""
nums = []
numCount = 0
count = 0
for val in sys.stdin.read().split():
# načítá čísla ze stdin a kontroluje zda se jedná o číslo.
    try:
        nums.append(float(val))
        # ukládá čísla do listu nums
        numCount = add(numCount,float(val))
        # počítá celkovou hodnotu všech čísel
        count = add(count,1)
        # počítá kolik čísel načte
    except ValueError:
        print("zadané špatné číslo: ", val)
# počítá průměr
prum = div(numCount,count)
prumExp = 0
# prochází list hodnot a umocňuje je a potom sčítá
for i in nums:
    prumExp = add(prumExp,expon(i,2))
# finální matematický počet
print(sqr(mul(div(1,sub(count,1)),sub(prumExp,mul(count,expon(prum,2)))),2))

