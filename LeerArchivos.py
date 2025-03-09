lectura = open("alumnos.txt", "r")#r de readable, a agrega datos, w reescribe


#Al querer probar cada uno hay que comentar los demas

print(lectura.read())#Lee el contenido completo
print(lectura.readline())#Lee linea por linea
print(lectura.readlines())#Lee con saltos de linea
print(lectura.readable())#Verifica si se puede abrir
print(lectura.readlines()[2])#Accede por indice

for alumno in lectura.readlines():
    print(alumno)

lectura.close()

lectura.write("\nDantucho")# Agrega con salto de linea

#Se puede crear un nuevo archivo
lectura = open("alumnos2.txt", "w")
lectura.write("Jose Jose")
lectura.close()