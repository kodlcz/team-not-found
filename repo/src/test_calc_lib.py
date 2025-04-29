## @file
#  @brief Unit testy pro matematické funkce v knihovně calc_lib.
#  @details Tento soubor obsahuje rozsáhlé testy pro funkce jako sčítání, odčítání, násobení, dělení,
#           faktoriál, mocniny, odmocniny, Fibonacciho posloupnost, absolutní hodnotu a validaci vstupů.

import unittest
from calc_lib import *

## @class TestMyMathLib
#  @brief Obsahuje testovací metody pro různé matematické operace.
class TestMyMathLib(unittest.TestCase):

    ## @brief Testy pro funkci add (sčítání).
    def test_add(self):
        self.assertEqual(add(1,1),2)
        self.assertEqual(add(-1,1),0)
        self.assertEqual(add(-1,-1),-2)
        self.assertEqual(add(430,142),572)
        self.assertEqual(add(-436,572),136)
        self.assertEqual(add(-574,-284),-858)
        self.assertEqual(add(1.5, 2.5), 4.0)
        self.assertNotEqual(add(4, 5), 4)

    ## @brief Testy pro funkci sub (odčítání).
    def test_sub(self):
        self.assertEqual(sub(1,1),0)
        self.assertEqual(sub(-1,1),-2)
        self.assertEqual(sub(-1,-1),0)
        self.assertEqual(sub(1,-1),2)
        self.assertEqual(sub(430,142),288)
        self.assertEqual(sub(-436,572),-1008)
        self.assertEqual(sub(-574,-284),-290)
        self.assertEqual(sub(436,-572),1008)
        self.assertEqual(sub(5.5, 2.5), 3.0)
        self.assertNotEqual(sub(25, 14), 3)

    ## @brief Testy pro funkci mul (násobení).
    def test_mul(self):
        self.assertEqual(mul(1,1),1)
        self.assertEqual(mul(-1,1),-1)
        self.assertEqual(mul(-1,-1),1)
        self.assertEqual(mul(430,142),61060)
        self.assertEqual(mul(-436,572),-249392)
        self.assertEqual(mul(-574,-284),163016)
        self.assertEqual(mul(2.5, 4), 10.0)
        self.assertNotEqual(mul(5, 4), 10)

    ## @brief Testy pro funkci div (dělení).
    def test_div(self):
        self.assertEqual(div(1,1),1)
        self.assertEqual(div(-1,1),-1)
        self.assertEqual(div(-1,-1),1)
        self.assertAlmostEqual(div(430,142),430/142)
        self.assertAlmostEqual(div(-436,572),-436/572)
        self.assertAlmostEqual(div(-574,-284),574/284)
        self.assertAlmostEqual(div(5, 2), 2.5)
        self.assertNotEqual(div(100, 2), 2.5)

    ## @brief Test dělení nulou.
    def test_div_zero(self):
        self.assertEqual(div(14,0),"chyba_2")

    ## @brief Testy pro funkci factorial.
    def test_factorial(self):
        self.assertEqual(factorial(1),1)
        self.assertEqual(factorial(0),1)
        self.assertEqual(factorial(2),2)
        self.assertEqual(factorial(6),720)
        self.assertEqual(factorial(10), 3628800)

    ## @brief Testy pro factorial s neplatnými vstupy.
    def test_factorial_value_err(self):
        self.assertEqual(factorial(-1),"chyba_4")
        self.assertEqual(factorial(3.56),"chyba_3")

    ## @brief Testy pro funkci expon (mocnění).
    def test_expon(self):
        self.assertEqual(expon(2, 3), 8)      
        self.assertEqual(expon(5, 0), 1)     
        self.assertEqual(expon(7, 1), 7)     
        self.assertEqual(expon(10, 2), 100)   
        self.assertEqual(expon(3, 4), 81)     
        self.assertEqual(expon(2, -2), 0.25)
        self.assertAlmostEqual(expon(9, 0.5), 3.0)
        self.assertNotEqual(expon(9, 2), 3)

    ## @brief Testy pro funkci sqr (odmocnina).
    def test_sqr(self):
         self.assertEqual(sqr(4,2),2)
         self.assertEqual(sqr(16,2),4)
         self.assertEqual(sqr(16,-2),0.25)
         self.assertAlmostEqual(sqr(36,3),36**(1/3))
         self.assertEqual(sqr(1, 5), 1)
         self.assertAlmostEqual(sqr(27, 3), 3)
         self.assertAlmostEqual(sqr(8, -3), 0.5)
         self.assertEqual(sqr(1, -1), 1)
         self.assertEqual(sqr(-16,2), "chyba_5")
         self.assertEqual(sqr(4,0), "chyba_2")
         self.assertAlmostEqual(sqr(2.25, 2), 1.5)
         self.assertEqual(sqr(25.0, 2), 5.0)
         self.assertNotEqual(sqr(25.0, 3), 5.0)

    ## @brief Testy pro Fibonacciho posloupnost.
    def test_fib(self):
        self.assertEqual(fib(0), 0)
        self.assertEqual(fib(1), 1)
        self.assertEqual(fib(2), 1)
        self.assertEqual(fib(5), 5)
        self.assertEqual(fib(10), 55)
        self.assertEqual(fib(15), 610)
        self.assertEqual(fib(-3), "chyba_4")

    ## @brief Testy pro absolutní hodnotu.
    def test_abs(self):
        self.assertEqual(abs(0), 0)
        self.assertEqual(abs(5), 5)
        self.assertEqual(abs(-5), 5)
        self.assertEqual(abs(123.456), 123.456)
        self.assertEqual(abs(-123.456), 123.456)
        self.assertNotEqual(abs(-435), -435)

    ## @brief Testy validace vstupních typů (např. string místo čísla).
    def test_value(self):
        self.assertEqual(add("a", 1), "chyba_1")
        self.assertEqual(sub(1, "b"), "chyba_1")
        self.assertEqual(mul("x", "y"), "chyba_1")
        self.assertEqual(div("10", 2), "chyba_1")
        self.assertEqual(factorial("5"), "chyba_3")
        self.assertEqual(expon("2", "3"), "chyba_1")
        self.assertEqual(sqr("9", 2), "chyba_1")
        self.assertEqual(sqr(9, "2"), "chyba_1")
        self.assertEqual(fib("7"), "chyba_1")
        self.assertEqual(abs("1"), "chyba_1")


## @brief Spuštění všech unit testů.
if __name__ == "__main__":
    unittest.main()
