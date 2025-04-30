"""
@file profiling.py
@author Adam Kadlec
@brief Výpočet výběrové směrodatné odchylky s náhodně generovanými vstupy a profilováním.
"""

import cProfile
import sys
import pstats
from calc_lib import *

# Počet hodnot lze libovolně měnit (např. 10, 1000, 1000000)
INPUT_SIZE = 10

def calculate_stddev():
    nums = []
    numCount = 0
    count = 0
    for val in sys.stdin.read().split():
        try:
            nums.append(float(val))
            numCount = add(numCount, float(val))
            count = add(count, 1)
        except ValueError:
            print("zadané špatné číslo: ", val)

    prum = div(numCount, count)
    prumExp = 0
    for i in nums:
        prumExp = add(prumExp, expon(i, 2))

    result = sqr(mul(div(1, sub(count, 1)), sub(prumExp, mul(count, expon(prum, 2)))), 2)
    print(result)

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

if __name__ == "__main__":
    run_profiled_calculations()
