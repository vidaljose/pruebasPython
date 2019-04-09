import re

nombre1 = "Sandra Lopez"
nombre2 = "Antonio Gomez"
nombre3 = "Maria Lopez"
nombre4 = "1234124312"

"""if re.match("\d",nombre4):
    print("Encontramos el numero")
else:
    print("No lo encontramos")"""

if re.search("Lopez",nombre1,re.IGNORECASE):
    print("Lo encontramos")
else:
    print("No lo encontramos")