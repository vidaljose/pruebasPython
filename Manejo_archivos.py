from io import open

#archivo_texto = open("archivo.txt","w")
#frase = "EStupendo dia para estudiar python \n es hoy"
#archivo_texto.write(frase)
#archivo_texto.close()


#archivo_texto = open("archivo.txt","r")
#texto = archivo_texto.read()
#archivo_texto.close()
#print(texto)
#lineas_texto = archivo_texto.readlines()
#archivo_texto.close()
#for i in lineas_texto:
#    print(i)
#archivo_texto = open("archivo.txt","a")
#archivo_texto.write("\nPython es genial")
#archivo_texto.close()
archivo_texto = open("archivo.txt","r+") #lectura y escritura
#archivo_texto.seek(len(archivo_texto.read())/2)
#print(archivo_texto.read())
#archivo_texto.write("Comienzo del texto")
#print(archivo_texto.readlines()[1])
lista_texto = archivo_texto.readlines();
lista_texto[1] = "Esta linea ha sido incluida desde el exterior \n"
archivo_texto.seek(0)
archivo_texto.writelines(lista_texto)
archivo_texto.close()
