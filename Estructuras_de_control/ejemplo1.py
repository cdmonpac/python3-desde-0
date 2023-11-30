#!/usr/bin/python3
# Realizado por Carlos Montoya =)

cont = 0;
for var in range(1,6):
    num = int(input("Dime un número: "))
    if num % 2 == 0:
        cont += 1
print("Has introducido",cont,"números pares.")