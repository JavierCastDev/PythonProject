texto = "Estamos programando en Python"

#Entre corchetes se coloca el indice al que se quiere acceder, los espacios cuentan como caracter
print(texto[0])

#Accede en orden inversa
print(texto[-1])

#Serie de caracteres a los que se quiere acceder, el 3 no se cuenta, muestra hasta el 2
print(texto[0:3])

#Imprime a partir del caracter que se le indique
print(texto[8:])

#Imprime de dos en dos en el rango que se le indica, en este caso 2 en 2 del 0 al 29
print(texto[0:29:2])

#Imprime de dos en dos hasta el final a partir del caracter 8
print(texto[8::2])

#Imprime en orden inversa
print(texto[::-1])



#Funciones habituales con strings

textoFuncion = "prueba estas funciones para strings"

#Muestra la cantidad de caracteres
print(len(textoFuncion))

#Coloca la primer letra en mayuscula
print(textoFuncion.capitalize())

#Reemplaza la parte del texto que le indiquemos por un texto nuevo
print(textoFuncion.replace("strings", "cadenas"))

#Muestra el indice de posicion del caracter que estamos buscando, diferencia minusculas y mayusculas
print(textoFuncion.index("p"))

#Muestra el texto en minusculas
print(textoFuncion.lower())

#Muestra el texto en mayusculas
print(textoFuncion.upper())

#Muestra si la variable es completamente minusculas
print(textoFuncion.islower())

#Muestra si la variable es completamente mayusculas
print(textoFuncion.isupper())

#Muestra si todos los caracteres son alfanumericos
print(textoFuncion.isalnum())

#Muestra si todos los caracteres son alfabeticos (los espacios no cuentan como alfabeto)
print(textoFuncion.isalpha())

#Muestra todas la funciones con las que se puede trabajar la variable
print(dir(texto))
