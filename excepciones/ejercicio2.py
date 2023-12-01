#!/usr/bin/python3
# Realizado por Carlos Montoya =)
      
cad = input("\nDime un número: ")
try:
    print(10/int(cad))
except ValueError:
    print ("No se pudo convertir a entero")
except ZeroDivisionError:
    print("No se puede dividir por cero")
else:
    print("Se ha producido otro error")
finally:
    print("Este es el final del programa")