print("Solicitar el ingreso de 10 números distintos y realizar lo siguiente:")
lista=[]
for i in range(10):
    lista.append(input("ingrese un número: ")) 

lista.sort()
#print (lista)

print("\n\na. Mostrar el mayor y menor.")
mayor=lista[0]
for a in range(0,10):
    if lista[a]>mayor:
        mayor=lista[a]
print("El número mayor es: ", mayor)
menor=lista[0]
posicion=0
for b in range (0,10):
    if lista[b]<menor:
        menor=lista[b]
        posicion=b
print("El número menor es: ", menor)

print("\n\nb. Listar los datos ordenados de forma descendente.")
lista.sort(reverse=True)
print(lista)

print("\n\nc. Mostrar la suma de los números.")
def sumar(lista):
    suma=0
    for numero in lista:
        suma+= numero
    return suma
print(sum(lista)) 

print("\n\nd. Indicar si la suma es un número primo.")