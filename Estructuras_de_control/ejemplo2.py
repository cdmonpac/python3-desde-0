#!/usr/bin/python3
# Realizado por Carlos Montoya =)

suma = 0;
for var in range(1,6):
    num = int(input("Dime un número: "))
    if num % 2 == 0:
        suma += num
print("La suma de los números pares es",suma)