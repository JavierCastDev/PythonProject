class persona:
    def __init__(self, nombre, edad, carrera, promedio):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.promedio = promedio

        # Funciones de clases

    def aprobado(self):
        if self.promedio > 5:
            print("Aprobaste")
        else:
            print("Reprobaste")