"""
    @file profiling.py
    @author Adam Kadlec
    @brief Výpočet výběrové směrodatné odchylky ze standardního vstupu pomocí vlastní matematické knihovny.
    @details Program načítá čísla ze standardního vstupu, vypočítá aritmetický průměr a následně výběrovou směrodatnou odchylku.

    @section usage Usage
    Spuštění programu s čísly zadanými na standardním vstupu. Program načítá čísla, počítá průměr a následně výběrovou směrodatnou odchylku.

    @param nums Seznam čísel, která se načítají ze vstupu.
    @param numCount Součet všech čísel načtených ze vstupu.
    @param count Počet načtených čísel.

    @return Vrací výběrovou směrodatnou odchylku pomocí výpisu na stdout.

"""
from calc_lib import *
import sys
nums = []
numCount = 0
count = 0
for val in sys.stdin.read().split():
## @brief načítá čísla ze stdin a kontroluje zda se jedná o číslo.
    try:
        nums.append(float(val))
        ## @brief ukládá čísla do listu nums
        numCount = add(numCount,float(val))
        ## @brief počítá celkovou hodnotu všech čísel
        count = add(count,1)
        ## @brief počítá kolik čísel načte
    except ValueError:
        print("zadané špatné číslo: ", val)
prum = div(numCount,count)
## @brief počítá průměr
prumExp = 0
for i in nums:
## @brief prochází list hodnot a umocňuje je a potom sčítá
    prumExp = add(prumExp,expon(i,2))
## @brief finální matematický počet
print(sqr(mul(div(1,sub(count,1)),sub(prumExp,mul(count,expon(prum,2)))),2))

