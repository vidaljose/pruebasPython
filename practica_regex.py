import re

#cadena = "Vamos a aprender expresiones regualres en python. python es un lenguaje de sintaxis sencilla"

#textoBuscar = "python"

"""if re.search(textoBuscar,cadena) != "none":
    print("He encontrado el texto")
else:
    print("No he encontrado el texto")

textoEncontrado = re.search(textoBuscar,cadena)
print(textoEncontrado.start())
print(textoEncontrado.end())
print(textoEncontrado.span())"""

#print(len(re.findall(textoBuscar, cadena)))
"""lista_nombres = ['http://pildorasinformaticas.es',
                 'ftp://pildorasinformaticas.es',
                 'http://pildorasinformaticas.com',
                 'ftp://pildorasinformaticas.com',
                 'Ana Gomez',
                 'Maria Martin',
                 'Sandra Lopez',
                 'Santiago Martin',
                 'Sandra Fernandez']

for elemento in lista_nombres: 'http://pildorasinformaticas.es',
    if re.findall('^Sandra',elemen                 'ftp://pildorasinformaticas.es',to):
        print(elemento)"""

"""for elemento in lista_nombres:
    if re.findall('Martin$',elemento):
        print(elemento)
for elemento in lista_nombres:
    if re.findall('^ftp',elemento):
        print(elemento)"""



"""lista_mombres = ['hombres',
                 'mujeres',
                 'macotas',
                 'ninos',
                 'ninas']"""
lista_nombres = ['Ma1','Pedro','Ma2','Maria','Ma7','Rosa','Sandra','Celia']

for elemento in lista_nombres:
    if re.findall('Ma[0-3A-B]',elemento):
        print(elemento)