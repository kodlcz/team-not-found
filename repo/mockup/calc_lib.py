def add(num1, num2):
    """
    @brief Sčítá dvě čísla.
    @param num1 První číslo (int nebo float).
    @param num2 Druhé číslo (int nebo float).
    @return Vrací součet dvou čísel, nebo chybovou hlášku (int, float nebo str).
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return "chyba 1"
    return num1 + num2


def sub(num1, num2):
    """
    @brief Odečítá dvě čísla.
    @param num1 První číslo (int nebo float).
    @param num2 Druhé číslo (int nebo float).
    @return Vrací rozdíl dvou čísel, nebo chybovou hlášku (int, float nebo str).
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return "chyba 1"
    return num1 - num2


def mul(num1, num2):
    """
    @brief Násobí dvě čísla.
    @param num1 První číslo (int nebo float).
    @param num2 Druhé číslo (int nebo float).
    @return Vrací součin dvou čísel, nebo chybovou hlášku (int, float nebo str).
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return "chyba 1"
    return num1 * num2


def div(num1, num2):
    """
    @brief Dělí dvě čísla.
    @param num1 Dělenec (int nebo float).
    @param num2 Dělitel (int nebo float).
    @return Vrací podíl dvou čísel, nebo chybovou hlášku (float nebo str).
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return "chyba 1"
    if num2 == 0:
        return "chyba 2"
    return num1 / num2


def factorial(num1):
    """
    @brief Vypočítá faktoriál čísla.
    @param num1 Celé číslo (int).
    @return Vrací faktoriál čísla, nebo chybovou hlášku (int nebo str).
    """
    if not isinstance(num1, int):
        return "chyba 3"
    if num1 < 0:
        return "chyba 4"
    result = 1
    while num1 > 1:
        result *= num1
        num1 -= 1
    return result


def power(num1, num2):
    """
    @brief Umocní číslo.
    @param num1 Základ (int nebo float).
    @param num2 Exponent (int nebo float).
    @return Vrací výsledek umocnění, nebo chybovou hlášku (float nebo str).
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return "chyba 1"
    return num1 ** num2


def root(num1, num2):
    """
    @brief Vypočítá odmocninu čísla.
    @param num1 Odmocňované číslo (int nebo float).
    @param num2 Kolikátá odmocnina (int nebo float).
    @return Vrací výsledek odmocnění, nebo chybovou hlášku (float nebo str).
    """
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return "chyba 1"
    if num2 == 0:
        return "chyba 2"
    return num1 ** (1 / num2)


def absolute(num1):
    """
    @brief Vrátí absolutní hodnotu čísla.
    @param num1 Číslo (int nebo float).
    @return Vrací absolutní hodnotu, nebo chybovou hlášku (float nebo str).
    """
    if not isinstance(num1, (int, float)):
        return "chyba 1"
    return abs(num1)


def fibonacci(num1):
    """
    @brief Vypočítá Fibonacciho číslo na dané pozici.
    @param num1 Pořadí v posloupnosti (int).
    @return Vrací číslo z Fibonacciho posloupnosti, nebo chybovou hlášku (int nebo str).
    """
    if not isinstance(num1, int):
        return "chyba 1"
    if num1 < 0:
        return "chyba 4"
    a, b = 0, 1
    for _ in range(num1):
        a, b = b, a + b
    return a
