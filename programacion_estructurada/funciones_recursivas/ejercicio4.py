#!/usr/bin/python3
# Realizado por Carlos Montoya =)

def factorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return (factorial(num - 1)) * num
print("\nFactorial de 5 es: ", factorial(5), "\n")