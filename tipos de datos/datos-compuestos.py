#creando una lista (se pueden modificar)
lista = ["Lucas Dalto","Soy Dalto",True,1.85]

#creando una tupla (no se pueden modificar)
tupla = ("Lucas Dalto","Soy Dalto",True,1.85)

#esto es válido 
#lista[3] = "Maquinola"

                        #todo para mostrarlo siempre va con corchete sin importar que la tupla vaya con "()"

#esto no 
#tupla[3] = "Maquinola"

#creando un conjunto (set) (no se accede a elementos por indice, no almacena datos duplicados)

conjunto = {"Lucas Dalto","Soy Dalto",True,1.85}

#print(conjunto[3]) --> no puede acceder al elemento 

#creando un diccionario (dict) (la estructura es key : value y separamos con comas)
diccionario = {
    'nombre' : 'Lucas Dalto',
    'canal' : 'Soy Dalto',
    'esta_emocionado' : True, 
    'altura' : 1.85,
    'dato_duplicado' : 'Soy Dalto'
    #key                #value
}
print(diccionario['altura'])
print(lista[3])
