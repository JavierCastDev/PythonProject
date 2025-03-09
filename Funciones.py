def miPrimerFuncion():
    print("Mi primer funcion")

miPrimerFuncion()


def miSegundaFuncion(nombre, edad):
    print("Mi nombre es " + nombre +" y tengo " + str(edad) + " años")


miSegundaFuncion("Javier", 27)


#Funciones con retorno

def valorMedio(num1, num2):
    media = (num1 + num2) / 2
    return media

respuesta = valorMedio(8, 4)
print(respuesta)


#Funciones recursivas

#Sucesion de Fibonacci

def fibonacci(i):
    if i == 0:
        return 0
    elif i == 1:
        return 1
    else:
        return fibonacci(i-1) + fibonacci(i-2)

print(fibonacci(8))