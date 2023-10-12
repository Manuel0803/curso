diccionario = {
    'nombre' : 'lucas',
    'apellido' : 'dalto',
    'subs' : 100000
}
#nos devuelve un objeto dict_item
claves = diccionario.keys()

#obteniendo un elemento con get(no me lanza una excepcion y si no encuentra nada el programa continua)
valor_de_kasdks = diccionario.get('kasdks')
print('Hola capo, el programa continua')

#eliminando todo del diccionario
#diccionario.clear()

#eliminando un elemento del diccionario
diccionario.pop('subs')

#obteniendo un elemento dict_items itinerable
diccionario_itinerable = diccionario.items()

print(diccionario_itinerable)