"""
@brief sčítá 2 čísla.
    
@param num1 první číslo (int or float).
@param num2 druhé číslo (int or float).
@return vrátí součet dvou čísel zároveň může vrátit chybu (int or float).
    
Tato funkce sčítá druhé číslo s prvním a kontroluje zda může dojít k chybě.
"""
def add(num1, num2):
    if not isinstance(num1,(int,float)) and isinstance(num2,(int,float)):
        return "chyba 1"
    return num1 + num2
"""
@brief odečítá 2 čísla.
    
@param num1 první číslo (int or float).
@param num2 druhé číslo (int or float).
@return vrátí rozdíl dvou čísel zároveň může vrátit chybu (int or float).
    
Tato funkce odečítá druhé číslo od prvního a kontroluje zda může dojít k chybě.
"""
def sub(num1, num2):
    if not isinstance(num1,(int,float)) and isinstance(num2,(int,float)):
        return "chyba 1"
    return num1 - num2
"""
@brief násobí 2 čísla.
    
@param num1 první číslo (int or float).
@param num2 druhé číslo (int or float).
@return vrátí násobek dvou čísel zároveň může vrátit chybu (int or float).
    
Tato funkce násobí druhé číslo s prvním a kontroluje zda může dojít k chybě.
"""
def sub(num1, num2):
    if not isinstance(num1,(int,float)) and isinstance(num2,(int,float)):
        return "chyba 1"
    return num1 * num2
"""
@brief dělí 2 čísla.
    
@param num1 první číslo (int or float).
@param num2 druhé číslo (int or float).
@return vrátí dělení dvou čísel zároveň může vrátit chybu (int or float).
    
Tato funkce dělí druhé číslo s prvním a kontroluje zda může dojít k chybě.
"""
def div(num1, num2):
    if not isinstance(num1,(int,float)) and isinstance(num2,(int,float)):
        return "chyba 1"
    if num2 == 0:
        return "chyba 2"
    return num1 / num2
"""
@brief faktorial čísla.
    
@param num1 první číslo (int).
@return vrátí faktorial čísla zároveň může vrátit chybu (int).
    
Tato funkce vykonává faktorial čísla a kontroluje zda může dojít k chybě.
"""
def faktorial(num1):
    if not isinstance(num1,(int)):
        return "chyba 3"
    if num1 < 0:
        return "chyba 4"
    num2 = 1
    while num1 > 1:
        num2 *= num1
        num1 -= 1
    return num2
"""
@brief umocňuje číslo.
    
@param num1 první číslo (int,float).
@param num2 druhé číslo (int,float)
@return vrátí mocninu čísla zároveň může vrátit chybu (int).

    
Tato funkce umodňuje první číslo pomocí druhého a kontroluje zda může dojít k chybě.
"""
def expon(num1, num2):
    if not isinstance(num1,(int,float)) and isinstance(num2,(int,float)):
        return "chyba 1"
    return num1 ** num2
"""
@brief odmocnina čísla.
    
@param num1 první číslo (int,float).
@param num2 druhé číslo (int,float).
@return vrátí odmocninu čísla zároveň může vrátit chybu (int).

    
Tato funkce odmocniňuje prvního čísla pomocí druhého a kontroluje zda může dojít k chybě.
"""
def sqrR(num1,num2):
    if not isinstance(num1,(int,float)) and isinstance(num2,(int,float)):
        return "chyba 1"
    return num1 ** (1/num2) 
"""
@brief absolutní hodnota čísla.
    
@param num1 první číslo (int).
@return vrátí absolutní hodnotu čísla zároveň může vrátit chybu (int).
    
Tato funkce vrací vždy kladné číslo a kontroluje zda může dojít k chybě.
"""
def abs(num1):
    if not isinstance(num1,(int,float)):
        return "chyba 1"
    if(num1 > 0):
        return num1
    return -num1
