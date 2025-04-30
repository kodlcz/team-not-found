"""
@file profiling.py
@author Adam Kadlec
@brief Výpočet výběrové směrodatné odchylky s náhodně generovanými vstupy a profilováním.
@details Tento skript načítá číselné hodnoty ze standardního vstupu, počítá výběrovou směrodatnou odchylku pomocí vlastní matematické knihovny
a zároveň měří výkon pomocí profileru cProfile.
"""

import cProfile
import sys
import pstats
from calc_lib import *

# Počet hodnot lze libovolně měnit (např. 10, 1000, 1000000)
INPUT_SIZE = 10

##
# @brief Funkce pro výpočet výběrové směrodatné odchylky ze vstupu.
# @details Načítá čísla ze stdin, počítá jejich součet, průměr a průměr čtverců, poté aplikuje vzorec pro směrodatnou odchylku.
# @return Výsledek (směrodatná odchylka) se vypíše na standardní výstup.
def calculate_stddev():
    nums = []  # seznam pro ukládání hodnot
    numCount = 0  # součet všech hodnot
    count = 0     # počet hodnot

    ## @brief Čtení a zpracování čísel ze vstupu
    for val in sys.stdin.read().split():
        try:
            nums.append(float(val))
            numCount = add(numCount, float(val))
            count = add(count, 1)
        except ValueError:
            print("zadané špatné číslo: ", val)

    prum = div(numCount, count)  # výpočet průměru
    prumExp = 0  # suma čtverců hodnot

    for i in nums:
        prumExp = add(prumExp, expon(i, 2))

    # Výpočet výběrové směrodatné odchylky dle vzorce
    result = sqr(mul(div(1, sub(count, 1)), sub(prumExp, mul(count, expon(prum, 2)))), 2)
    print(result)

##
# @brief Spuštění výpočtu s měřením výkonnosti pomocí cProfile.
# @details Profiluje funkci calculate_stddev a ukládá výstup do souboru profiling_output.txt.
def run_profiled_calculations():
    profiler = cProfile.Profile()
    profiler.enable()

    calculate_stddev()

    profiler.disable()
    stats = pstats.Stats(profiler)
    with open('profiling_output.txt', 'w') as f:
        stats.stream = f
        stats.sort_stats('cumulative')  # nebo 'time' dle potřeby
        stats.print_stats()

##
# @brief Vstupní bod programu.
# @details Spouští profilovaný výpočet směrodatné odchylky.
if __name__ == "__main__":
    run_profiled_calculations()
