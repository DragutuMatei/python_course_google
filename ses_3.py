# Să se scrie o funcție care primește un număr nedefinit de parametrii și să se calculeze suma parametrilor care reprezintă numere întregi sau reale.
def my_function(*args, **kwargs):
    sum = 0 
    for arg in args:
        if type(arg) == int or type(arg) == float:
            sum += arg
    
    return sum


print(my_function(1, 5, -3,'abc2', [12, 56, 'cad']))
print(my_function())
print(my_function(2, 4, 'abc', param_1=2) )
# ===============================================================================================================================================================

# ● Să se scrie o funcție recursivă care primește ca parametru o lista cu numere întregi și returnează: 
# ○ suma totală a numerelor
# ○ suma numerelor pare
# ○ suma numerelor impare

def recursive_function(lista=[]):
    if not lista:
        return 0, 0, 0

    suma_totala, suma_par, suma_impar = recursive_function(lista[1:])
    
    suma_totala += lista[0]
    
    if lista[0] % 2 == 0:
        suma_par += lista[0]
    else:
        suma_impar += lista[0]
        
    return suma_totala, suma_par, suma_impar


print(recursive_function([1,2,3,4,5,6,7,8,9,10]))

# total: 1+2+3+4+5+6+7+8+9+10=55
# par: 2+4+6+8+10=30
# impar: 1+3+5+7+9=25

# ===============================================================================================================================================================


# Să se scrie o funcție care citește de la tastatură și returnează valoarea dacă aceasta este un număr întreg, altfel returnează valoarea 0.

def citire_si_testare():
    n = input("Introdu un numar: ")
    # if type(n) == int or type(n) == float:
    #     return n
    # else:
    #     return 0
    try:
        return int(n)
    except ValueError as e:
        return 0
    
print(citire_si_testare())
        
        