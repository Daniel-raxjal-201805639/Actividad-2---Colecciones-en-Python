print("Agregar en una tupla 8 textos y realizar lo siguiente:")
tupla=["uno", "salsas", "plantas", "EFPEM", "murcielago", "Sandia", "python", "Visual"]

print("\n\na. Mostrar los textos existentes en la tupla (un elemento por línea):")
i=0
while i<len(tupla):
    print(tupla[i])
    i+=1

print("\n\nb. Mostrar los textos que posee la tupla, todas las letras en mayúscula.")
for i in range(len(tupla)):
    print(tupla[i].upper())

print("\n\nc. Mostrar los textos que posee la tupla, todas las letras en minúscula")
for i in range(len(tupla)):
    print(tupla[i].lower())

print("\n\nd. Mostar los textos que finalizan con la letra “s” ya sea con mayúscula o minúscula.")
for i in range(len(tupla)):
   if(tupla[i][len(tupla[i])-1:len(tupla[i])]) == "s" or (tupla[i][len(tupla[i])-1:len(tupla[i])]) == "S":
       print(tupla[i])

print("\n\ne. Contar la cantidad de vocales existentes en los textos, mostrar la información de la siguiente forma:a = __, e = __, i=__, o=__, u=__, total de vocales = __")
h=0
def contar_vocales():
  vocal=["a","e","i","o","u","A","E","I","O","U"]
  cont = 0
  for i in vocal:
    for j in txt:
      if(i==j):
        cont+=1
        total = cont
        #print("El número de voclaes es: ", cont)

  print("total de vocales ", total)

while h<len(tupla):
    txt = tupla[h]
    contar_vocales()
    h+=1





