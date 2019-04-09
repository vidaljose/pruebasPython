"""def numero_par(num):
    if num % 2 == 0 :
        return True

numeros = [17,24,7,39,8,51,92]

print(list(filter(lambda numero_par: numero_par%2 == 0,numeros)))"""

class Empleado:
    def __init__(self,nombre,cargo,salario):
        self.nombre = nombre
        self.cargo = cargo
        self.salario = salario

    def __str__(self):
        return f"{self.nombre} que trabaja como {self.cargo} y tiene un salario de {self.salario}$"

listaEmpleados = [
    Empleado("Juan","Director",75000),
    Empleado("Ana","Presidenta",85000),
    Empleado("Antonio","Administrativo",25000),
    Empleado("Sara","Secretaria",27000),
    Empleado("Mario","Botones",21000)
]
#imprime una lista de objetos
salarios_altos = filter(lambda empleado : empleado.salario>50000,listaEmpleados)
for i in salarios_altos:
    print(i)