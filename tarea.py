#TAREA:
# 1º Dada la palabra cuente cuantas veces esta esa palabra

# 2º Dada la cadena, decir si todos los elementos son letras

# 3º dada la cadena contar las consonantes



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("\n1º-----\"------------------------------Dada la palabra cuente cuantas veces esta esa palabra---------------------------------------------------------\n")

print("La palabra que desea cuantificar: Murcielago \n ")
palabra="Murcielagooo"

palabra=palabra.lower() #Aqui se comvierten los digitos de la palabra en minuscula, con el fin de evitar errores

ContandoletraA=palabra.count("a") #funcion count cuenta cuantas veces un elemento de una cadena se repite, 
                                    #se escribe el nombre de la variable, seguida de punto y la palabra count(), dentro del parentesis va la leta que deseo contar
ContandoletraE=palabra.count("e")
ContandoletraI=palabra.count("i")
ContandoletraO=palabra.count("o")
ContandoletraU=palabra.count("u")
ContandoletraM=palabra.count("m")
ContandoletraL=palabra.count("l")
ContandoletraG=palabra.count("g")
ContandoletraR=palabra.count("r")
ContandoletraC=palabra.count("c")
print("Letra a: ",ContandoletraA,"Letra e: ",ContandoletraE,"Letra i: ",ContandoletraI,"Letra o: ",ContandoletraO,"Letra U: ",ContandoletraU)
print("Letra g: ",ContandoletraG,"Letra r: ",ContandoletraR,"Letra c: ",ContandoletraC,"Letra l: ",ContandoletraL,"Letra m: ",ContandoletraM)


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("\n2º-----------------------------------------Dada la cadena, decir si todos los elementos son letras---------------------------------------------------\n")

cadena=input("Ingrese la cadena: ")

if(cadena.isalpha()==True): #isalpha analiza la cadena y nos retorna un true si todos los caracteres son valores alfabeticos, si hay al menos un elemento que no sea del alfabeto nos arroja un false
    print("Todos los valores de la cadena son letras. congratulations")
    long=len(cadena)
    print("La totalidad de caracteres es ",long)
else:
    print("Al menos uno de los caracteres no es una letra. Puede ser espacio, simbolo o numero\n")

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
print("\n3º-----------------------------------------Dada la cadena contar las consonantes---------------------------------------------------\n")

import re

consonantes=input("Ingrese las palabras de las que desea contar las consonantes: \n")
consonantes=consonantes.lower() #convertir en minusculas
consi=re.findall(r"[qwrtyplkjhgfdszxcvbnm]",consonantes) #usar el findall para encontrar una cadena dentro de la cadena que se ingresa, r"[]", lo que esta dentro de las comillas es lo que deseo agrupar, 
                                                        #y luego de la coma es la cadena a la que le estoy sacando la cadena especifica
print("Las consonantes son: ",consi)
print("El numero de cosonantes son: ",len(consi))
