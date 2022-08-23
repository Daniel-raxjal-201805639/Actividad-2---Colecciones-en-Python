print("Solicitar al usuario 15 nombres, almacenarlos en una lista y realizar lo siguiente:")
lista=[]
for i in range(4):
    lista.append(input("ingrese un nombre: ")) 

lista.sort()
#print (lista)

print("\n\na. Listar nombres ordenados alfabéticamente, de forma ascendente:")
lista.sort()
print(lista)

print("\n\nb. Listar los nombres ordenados alfabéticamente, de forma descendente:")
lista.sort(reverse=True)
print(lista)

print("\n\nc. Mostrar el promedio de las longitudes de los nombres:")

print("\n\nd. Listar únicamente los nombres que finalizan con vocal:")

