empleados = {"Javier", "Capichon", "Dante"}

#Los sets no tienen un orden definido, no se puede acceder a los indices
#No se pueden repetir elementos, no mostrara error pero no lo agregara como elemento nuevo

empleados.add("Dantucho")#Agrega un elemento
print(empleados)

nuevosEmpleados = {"Capiguapo"}

empleados.update(nuevosEmpleados)#Agrega el contenido de un set a otro
print(empleados)

empleados.remove("Javier")#Elimina un elemento
print(empleados)

empleados.remove("Dantucho")#Elimina un elemento, tener cuidado de que el elemento si este en el set, si no arroja error
print(empleados)

empleados.discard("Pelucho")#Si el elemento esta, lo elimina, si no, sigue el resto del codigo
print(empleados)

empleados.pop()#Elimina un elemento aleatorio
print(empleados)