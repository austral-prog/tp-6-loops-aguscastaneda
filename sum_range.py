# Replace the "ANSWER HERE" for your answer

def sum_to_n(n):
    """
    Retorna la suma de todos los enteros desde 1 hasta n (inclusive).
    Si n <= 0, retorna 0.

    Ejemplo: sum_to_n(5) -> 15  (1+2+3+4+5)
    """
    suma = 0 
    if n != 0:
        for i in range(0, n):
            suma += (i + 1)
        return suma
    else:
        return 0 


def sum_evens(n):
    """
    Retorna la suma de todos los numeros pares desde 1 hasta n (inclusive).
    Si n <= 0, retorna 0.

    Ejemplo: sum_evens(10) -> 30  (2+4+6+8+10)
    """
    
    suma = 0
    if n != 0:
        for i in range(1, n + 1):
            if i % 2 == 0:
                suma += i
        return suma
    else:
        return 0        
        

def factorial(n):
    """
    Retorna el factorial de n (n!).
    Si n <= 0, retorna 1.

    Ejemplo: factorial(5) -> 120  (1*2*3*4*5)
    """
    
    fact = 1
    if n != 0:
        for i in range(1, n + 1):
            fact *= i
        return fact
    else:
        return 1 
