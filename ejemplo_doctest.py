import doctest

def areaTriangulo(base,altura):
    """
    Calcula el area de un triangulo
    >>> areaTriangulo(3,6)
    'El area del triangulo es: 9.0'
    """
    return "El area del triangulo es: " + str((base*altura)/2)

def compruebaMail(mailUsuario):
    """
    Evaluea un mail, buscando la @

    >>> compruebaMail('vidaljose2004@gmail.com')
    True
    
    >>> compruebaMail('vidaljose2004gmail.com@')
    False

    >>> compruebaMail('vidaljose2004gmail.com')
    False
    
    >>> compruebaMail('vidaljose2004@gmail@.com')
    False

    """
    arroba = mailUsuario.count('@')
    if (arroba != 1 or mailUsuario.rfind('@')==(len(mailUsuario)-1) or mailUsuario.find('@')==0 ):
        return False
    else:
        return True

#print(areaTriangulo(3,6))
doctest.testmod()