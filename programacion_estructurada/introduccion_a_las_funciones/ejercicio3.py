#!/usr/bin/python3
# Realizado por Carlos Montoya =)

def factorial(n):
    """Calcula el factorial de un número"""
    resultado = 1
    for i in range(1,n+1):
        resultado*=i
    return resultado

num = int(input("Dame un número: "))
print(factorial(num))