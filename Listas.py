edades = [10, 57, 89, 60]
nombres = ["Javier", "Abigail", "Capi"]
lista = [26, "Capi", True]

#Agregar elemento a una lista

nombres.insert(0, "Dante")#Especifica en que indice agregarlo
print(nombres)
edades.append(20)#Lo agrega al final por default
print(edades)

#Eliminar elemento de una lista

edades.remove(57)#Se especifica el contenido del elemento a eliminar
print(edades)
edades.__delitem__(0) #Se ingresa el indice
print(edades)
edades.clear()#Elimina todos los elementos de una lista
print(edades)

#Obtener el indice del elemento
print(nombres.index("Capi"))

#Cambiar un elemento por otro mediante el indice
nombres[0] = "Panino"
print(nombres)



#Funciones habituales con listas

print(nombres.count("Capi")) #Cuenta cuantas veces esta ese valor en la lista

edades.extend(nombres)#Agrega a una lista los datos que haya en otra
print(edades)

nombres.reverse()#Revierte el orden de una lista
print(nombres)

nombres.sort()#Ordena la lista
print(nombres)

datos = nombres.copy() #Copia todos los datos de una lista a otra variable
print(datos)