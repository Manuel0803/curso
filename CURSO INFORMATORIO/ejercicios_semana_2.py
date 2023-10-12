#Ejercicio 1 

# edad_usuario = int(input('Ingresa tu edad: '))

# if edad_usuario >= 18:
#      print('Sos mayor de edad.')
# else:
#     print('Sos menor de edad.')

#Ejercicio 2

#numero_entero = int(input('Ingresa un numero entero: '))
#if numero_entero >= 0: 
#    print('El numero entero es positivo')
#    if numero_entero == 0:
#        print('y vale 0')
#elif numero_entero < 0:
#    print('El numero entero es negativo')
#else:
#    print('Usted no ingreso un numero entero, intente nuevamente.')
    
#Ejercicio 3

# numero_ingresado_a, numero_ingresado_b = int(input('Ingrese un numero: ')), int(input('ingrese otro numero: '))
# if numero_ingresado_a > numero_ingresado_b:
#      print(f'El numero {numero_ingresado_a} es mayor que {numero_ingresado_b}')
# elif numero_ingresado_a < numero_ingresado_b:
#      print(f'El numero {numero_ingresado_a} es menor que {numero_ingresado_b}')
# else: 
#      print(f'Los numeros {numero_ingresado_a} y {numero_ingresado_b} son iguales')

#Ejercicio 4

# notas_del_usuario = int(input('Ingrese su nota (del 0 al 10):  '))
# if notas_del_usuario < 6:
#     print('Usted esta desaprobado.')
# elif notas_del_usuario < 8:
#     print('Usted aprobo con lo justo.')
# elif notas_del_usuario < 10:
#     print('Genial venis muy bien.')
# else:
#     print('Excelente estas aprobado.')

#ejercicio 5

# numero_del_usuario = int(input('Ingrese por favor un numero entero: '))
# if numero_del_usuario % 2 == 0:
#     print('El numero es par')
# else:
#     print('El numero es impar')

#ejercicio 6

# numero_entero_usuario = int(input('Ingrese por favor un numero entero: '))
# if numero_entero_usuario % 2 == 0 and numero_entero_usuario % 3 == 0:
#     print('Es multiplo de ambos')
# elif numero_entero_usuario % 2 == 0:
#     print('Es multiplo de 2')
# else:
#     print('Es multiplo de 3')

#ejercicio 7

# caracter_ingresado_por_usuario = input('Ingrese un caracter de tipo mayuscula, minuscula, número o un especial: ')
# if caracter_ingresado_por_usuario.isupper() == True:
#      print('Usted ingreso un caracter Mayuscula.')
# elif caracter_ingresado_por_usuario.islower() == True:
#     print('Usted ingreso un caracter Minuscula.')
# elif caracter_ingresado_por_usuario.isnumeric() == True:
#     print('Usted ingreso un número.')
# else:
#     print('Usted ingreso un caracter especial.')

#ejercicio 8

# dato_ingresado = input('Ingresa una oracion o palabra cualquiera: ')
# if "a" in dato_ingresado or "A" in dato_ingresado:
#     print(f'Se encuentra la letra A en {dato_ingresado}.')
# else:
#     print(f'No se encuentra la letra A en {dato_ingresado}.')

#ejercicio 9

# numero_a, numero_b, numero_c = int(input('Ingrese un numero: ')), int(input('Ingrese un segundo numero: ')), int(input('Ingrese un tercer numero: '))
# if numero_a > numero_b and numero_a > numero_c:
#     print(f'El primer numero ingresado {numero_a} es mayor que {numero_b} y {numero_c}')
# elif numero_b > numero_a and numero_b > numero_c:
#     print(f'El segundo numero ingresado {numero_b} es mayor que {numero_a} y {numero_c}')
# else:
#     print(f'El tercer numero ingresado {numero_c} es mayor que {numero_a} y {numero_b}')
    
#ejercicio 10

# letra_ingresada_usuario = input('Por favor ingrese una letra: ').lower()
# if letra_ingresada_usuario == 'a' or letra_ingresada_usuario == 'e' or letra_ingresada_usuario == 'i' or letra_ingresada_usuario == 'o' or letra_ingresada_usuario == 'u':
#     print('Usted ingreso una vocal')
# else:
#     print('Usted ingreso una consonante')

#ejercicio 11

# numeros_a, numero_b = int(input('Ingrese un numero: ')), int(input('Ingrese otro numero: '))
# resultado_suma = numeros_a + numero_b
# if resultado_suma % 2 == 0:
#     print(f'El resultado de la suma entre {numeros_a} y {numero_b} es {resultado_suma}')
# else:
#     print(f'El resultado de la suma entre {numeros_a} y {numero_b} no puede mostrarse ya que no es par.')

#PARTE 2 SEMANA 2

#ejercicio 1

# fruteria = {
#     'Bananas':'$500 el kg',
#     'Manzanas':'$700 el kg',
#     'Naranjas':'$650 el kg'
# }
# print(fruteria)

#ejercicio 2

# nombres_ciudades = ['Resistencia', 'Corrientes', 'Mendoza']
# print(nombres_ciudades)
# nombres_ciudades.append('Chubut')
# print(nombres_ciudades)

#ejercicio 3

# paises_nombres = ['Islandia', 'Noruega', 'Indonesia']
# print(paises_nombres[1])

#ejercicio 4

# nombres_de_personas_datos = {
#     'Julian':'38 años',
#     'Pepe':'25 años',
#     'Matias':'18 años'
# }
# print(f'La tercer persona del diccionario tiene {nombres_de_personas_datos["Matias"]}   ')

#ejercicio 5

# conjunto_numeros = {1, 2, 4, 5, 6, 7, 8, 9, 10}
# valores_max = max(conjunto_numeros)  
# if valores_max == 10:
#     print(f'El entero mayor en {conjunto_numeros} es {valores_max}')
    
#ejercicio 6

# conjunto_de_numeros = [1, 3, 5, 7, 9] 
# print(len(conjunto_de_numeros))

#ejercicio 7

# ciudades_poblaciones = {
#     'Resistencia':'1.142.963 habitantes.',
#     'Buenos Aires':'17.569.053 habitantes.',
#     'Tierra del Fuego':'190.641.'
# }
# print(ciudades_poblaciones)
# ciudades_poblaciones['Posadas'] = '383.543 habitantes'
# print(ciudades_poblaciones)

#ejercicio 8
# lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(lista_numeros)
# lista_numeros.reverse()
# print(lista_numeros)

#ejercicio 9

# nombres_paises = ['Uruguay', 'Islandia', 'Chile']
# print(nombres_paises)
# nombres_paises.sort()
# print(nombres_paises)

#ejercicio 10

# lista_frutas = ['Banana', 'Manzana', 'Uva']
# print(lista_frutas)
# lista_frutas.pop(1)
# print(lista_frutas)    

#ejercicio 11

# lista_animales = ['Chita', 'Conejo', 'Vaca']
# print(lista_animales)
# lista_animales.insert(0, 'Cerdo')
# print(lista_animales)    

#ejercicio 12
# lista_de_paises = ['Bolivia', 'Paraguay', 'Italia']
# print(lista_de_paises)
# lista_de_paises.pop(1)
# print(lista_de_paises)
# lista_de_paises.insert(1, 'Estonia')
# print(lista_de_paises)

#ejercicio 13 

# lista_de_colores = ['Azul', 'Verde', 'Naranja']
# print(lista_de_colores)
# lista_de_colores.extend(['Rojo','Fucsia'])
# print(lista_de_colores)

#ejercicio 14

# tupla_de_numeros = (1, 2, 3, 4, 5)
# print(tupla_de_numeros)
# suma_de_tupla = sum(tupla_de_numeros)
# print(suma_de_tupla)