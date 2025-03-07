#Solicitar datos al usuario

edad = input("Ingresa tu edad: ")
print(type(edad))
nombre = input("Ingresa tu nombre: ")
print(type(nombre))
print("Te llamas " + nombre + " y tienes " + edad + " años.")


#Especificar el tipo de dato que se espera
edad2 = int(input("Ingresa tu edad: "))
print(type(edad2))
nombre2 = str(input("Ingresa tu nombre: "))
print(type(nombre2))
print("Te llamas " + nombre2 + " y tienes " + str(edad2) + " años.") #Al agregar str se evita que arroje una excepcion al compilar
