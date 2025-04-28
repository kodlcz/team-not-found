"""
    @file calc_lib.py
    @brief knihovna matematických funkcí
    @details jsou volány funkce které načítají jedno nebo dvě čísla a ověřuje jejich integritu s tím že vrací jedno číslo jako int nebo float.
    @author Adam Kadlec
    """
def add(num1, num2):
    """
    @brief Sčítá dvě čísla.
    @param num1 První číslo (int nebo float).
    @param num2 Druhé číslo (int nebo float).
    @return Vrací součet dvou čísel, nebo chybovou hlášku (int, float nebo str).
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return "chyba_1"
    return num1 + num2


def sub(num1, num2):
    """
    @brief Odečítá dvě čísla.
    @param num1 První číslo (int nebo float).
    @param num2 Druhé číslo (int nebo float).
    @return Vrací rozdíl dvou čísel, nebo chybovou hlášku (int, float nebo str).
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return "chyba_1"
    return num1 - num2


def mul(num1, num2):
    """
    @brief Násobí dvě čísla.
    @param num1 První číslo (int nebo float).
    @param num2 Druhé číslo (int nebo float).
    @return Vrací součin dvou čísel, nebo chybovou hlášku (int, float nebo str).
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return "chyba_1"
    return num1 * num2


def div(num1, num2):
    """
    @brief Dělí dvě čísla.
    @param num1 Dělenec (int nebo float).
    @param num2 Dělitel (int nebo float).
    @return Vrací podíl dvou čísel, nebo chybovou hlášku (float nebo str).
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return "chyba_1"
    if num2 == 0:
        return "chyba_2"
    return num1 / num2


def factorial(num1):
    """
    @brief Vypočítá faktoriál čísla.
    @param num1 Celé číslo (int).
    @return Vrací faktoriál čísla, nebo chybovou hlášku (int nebo str).
    """
    if not isinstance(num1, int):
        return "chyba_3"
    if num1 < 0:
        return "chyba_4"
    num = 1
    while num1 > 1:
        num *= num1
        num1 -= 1
    return num


def expon(num1, num2):
    """
    @brief Umocní číslo.
    @param num1 Základ (int nebo float).
    @param num2 Exponent (int nebo float).
    @return Vrací výsledek umocnění, nebo chybovou hlášku (float nebo str).
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return "chyba_1"
    return num1 ** num2


def sqr(num1, num2):
    """
    @brief Vypočítá odmocninu čísla.
    @param num1 Odmocňované číslo (int nebo float).
    @param num2 Kolikátá odmocnina (int nebo float).
    @return Vrací výsledek odmocnění, nebo chybovou hlášku (float nebo str).
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return "chyba_1"
    if num2 == 0:
        return "chyba_5"
    return num1 ** (1 / num2)


def absolute(num1):
    """
    @brief Vrátí absolutní hodnotu čísla.
    @param num1 Číslo (int nebo float).
    @return Vrací absolutní hodnotu, nebo chybovou hlášku (float nebo str).
    """
    if not isinstance(num1, (int, float)):
        return "chyba_1"
    if num1 < 0:
        num1 *= -1
    return num1


def fib(num1):
    """
    @brief Vypočítá Fibonacciho číslo na dané pozici.
    @param num1 Pořadí v posloupnosti (int).
    @return Vrací číslo z Fibonacciho posloupnosti, nebo chybovou hlášku (int nebo str).
    """
    if not isinstance(num1,(int,float)):
        return "chyba_1"
    if num1 < 0:
        return "chyba_4"
    num = 0 
    num0 = 1
    if num1 == 0:
        return 0
    while num1 > 0:
            num00 = num
            num += num0
            num0 = num00
            num1 -= 1
    return num
