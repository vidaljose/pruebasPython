from modulos import funciones_matematicas

class Areas:
    def areaCuadrado(self,lado):
        """Calcula el area de un cuadrado elevando al cuadrado el parametro"""
        return "El area del cuadrado es: "+ str(lado*lado)
        
    def areaTriangulo(self,base,altura):
        """Calcula el area de un triangulo jejejej """
        return "El area del triangulo es: "+str((base*altura)/2)


# print(areaCuadrado(5))
# print(areaCuadrado.__doc__)
help(funciones_matematicas)

