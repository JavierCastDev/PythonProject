#Maneja clave y valor
#Las claves no se pueden modificar, los valores si
from Tuplas import alumnos

producto = {"Cerrojo": 120, "Puerta": 1250, "Ventana": 500}
print(producto)

#Solo se puede acceder a las claves, no a los valores
print(producto["Cerrojo"])

print(producto.get("Madera", "No existe"))#Busca la clave, si no existe muestra el texto definido

#Modificar el valor de un elemento
producto["Cerrojo"] = 125
print(producto["Cerrojo"])

#Agrega una pareja al diccionario
producto["Pegamento"] = 50
print(producto)

#Eliminar pareja, debe estar forzosamente
del producto["Cerrojo"]
print(producto)