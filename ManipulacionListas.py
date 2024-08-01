
numeros = [4, 2, 9, 1, 5, 6]

nuevo_numero = 10
numeros.append(nuevo_numero)  
print(f"Lista después de agregar {nuevo_numero}: {numeros}")

numeros.pop(0)  
print(f"Lista después de eliminar el primer elemento: {numeros}")

numeros.sort()  
print(f"Lista después de ordenar en orden ascendente: {numeros}")

numeros.reverse()  
print(f"Lista después de invertir: {numeros}")


print(f"Lista final modificada: {numeros}")