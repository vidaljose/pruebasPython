import pickle
#lista_nombre = ["Pedro","Ana","Maria","Isabel"]
#fichero_binario = open("lista_nombre","wb")# wb es escirtura bianaria
#pickle.dump(lista_nombre,fichero_binario)
#fichero_binario.close()
#del(fichero_binario)

fichero = open("lista_nombre","rb")
lista = pickle.load(fichero)
print(lista)
