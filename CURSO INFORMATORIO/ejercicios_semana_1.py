# ejercicio 1
# nombre_usuario = input('Ingresa tu nombre: ')
# print(f'el nombre de usuario es: {nombre_usuario}')

#ejercicio 2
#nombre_usuario_bienvenida = input('Ingresa tu nombre: ')
#print(f'!!Bienvenido {nombre_usuario}¡¡')

#ejercicio 3
#edad_usuario = int(input('Ingresa tu edad: '))
#print(f'Edad: {edad_usuario} años')

#ejercicio 4
#calculos = int(input('Ingrese numero a: '))
#calculos_b = int(input('Ingrese numero b: '))
#sumatoria = calculos + calculos_b
#print(f'El calculo es: {sumatoria}')

#ejercicio 5
#calculos = int(input('Ingrese el dividendo: '))
#calculos_b = int(input('Ingrese el divisor: '))
#division = calculos / calculos_b 
#resto = calculos % calculos_b
#print(f'La division entre {calculos} y {calculos_b} da un cociente {division} con un resto de {resto}')

#ejercicio 6
#radio_ingresado = int(input('Ingrese el radio de un circulo: '))
#pi = 3.1416
#calculo_area = pi * radio_ingresado **2 
#print(f'El area del circulo es: {calculo_area}')

#ejercicio 7
#altura_triangulo = float(input('Ingrese la medida de la altura del triangulo: '))
#base_triangulo = float(input('Ingrese la medida de la base del triangulo: '))
#calculo_area = base_triangulo * altura_triangulo / 2  
#print(f'el area del triangulo es {calculo_area}')

#ejercicio 8
#pi = 3.14159
#radio_circulo = float(input('Ingrese el radio de un circulo: '))
#calculo_diametro = 2 * radio_circulo
#calculo_circunferencia = calculo_diametro * pi
#calculo_area =  pi * radio_circulo
#print(f'El diametro del circulo es: {calculo_diametro}')
#print(f'La circunferencia del circulo es: {calculo_circunferencia}')
#print(f'El area del circulo es: {calculo_area}')
#consulta por tener numeros tan altos es decir tener numeros mas precisos redondear

#ejercicio 9
#numero_a = float(input('Ingrese numero a: '))
#numero_b = float(input('Ingrese numero b: '))
#calculos_suma = numero_a + numero_b 
#calculos_multiplicacion = numero_a * numero_b
#calculos_division = numero_a / numero_b
#print(f'La suma entre a y b es {calculos_suma}')
#print(f'La multiplicacion entre a y b es {calculos_multiplicacion}')
#print(f'La division entre a y b es {calculos_division}')

#ejercicio 10
#cantidad_dolares = float(input('Ingrese cantidad de dolares: '))
#cambio_dolar_euro = 0.84
#calculo = cantidad_dolares * cambio_dolar_euro
#print(f'La cantidad de euros que usted tiene es: {calculo}')

#ejercicio 11
#palabras_usuario = input('Ingresa una frase: ')
#cantidad_letras = len(palabras_usuario)
#print(f'La cantidad de letras que tiene su frase son: {cantidad_letras}')

# # #ejercicio 12
# datos_usuario_dia_mes_año = input('Ingrese su fecha de nacimiento en formato dd/mm/aaaa: ')
# datos_usuario = datos_usuario_dia_mes_año.split('/')
# fecha_actual = input('ingrese fecha actual en formato dd/mm/aaaa ')
# fecha_actual_lista = fecha_actual.split('/')
# calculo_edad_dia = abs(int(fecha_actual_lista[0]) - int(datos_usuario[0]))
# calculo_edad_mes = abs(int(fecha_actual_lista[1]) - int(datos_usuario[1]))
# calculo_edad_anio = abs(int(fecha_actual_lista[2]) - int(datos_usuario[2]))
# if calculo_edad_mes <= 1 and calculo_edad_dia <=1:
#      print(f'Usted tiene {calculo_edad_anio} años con {calculo_edad_mes} mes y {calculo_edad_dia } dia')
# elif calculo_edad_mes <=1:
#      print(f'Usted tiene {calculo_edad_anio} años con {calculo_edad_mes} mes y {calculo_edad_dia } dias')
# elif calculo_edad_dia <=1:
#      print(f'Usted tiene {calculo_edad_anio} años con {calculo_edad_mes} meses y {calculo_edad_dia } dia')
# else:
#      print(f'Usted tiene {calculo_edad_anio} años con {calculo_edad_mes} meses y {calculo_edad_dia } dias')


#tengo un problema cuando el resultado es negativo.

# # ejercicio 13
# datos_usario = input('Ingresa tu nombre y tu edad: ')
# datos = datos_usario.split()
# calculos = int(datos[1]) + 10 
# print(f'Dentro de 10 años {datos[0]} tendras {calculos} años') 

#ejercicio 14
#solicitar_numero_usuario = int(input('Ingrese un numero entero: '))
#calculo_doble = solicitar_numero_usuario * 2
#calculo_triple = solicitar_numero_usuario * 3 
#print(f'El doble de {solicitar_numero_usuario} es {calculo_doble} y el triple es {calculo_triple}')

#ejercicio 15
#temperatura_grados_c = float(input('Ingrese temperatura actual en grados Celsius: '))
#calculo_gradosc_gradosf = temperatura_grados_c * 1.8 + 32
#print(f'La temperatura actual es de: {calculo_gradosc_gradosf} grados Farenheit')

#ejercicio 16
#datos_peso_usuario = float(input('Ingrese su peso en kilogramos: '))
#datos_altura_usuario = float(input('Ingrese su altura en metros: '))
#calculo_imc = datos_peso_usuario / datos_altura_usuario ** 2 
#print(f'Su indice de masa corporal (IMC) es de {calculo_imc}')

#ejercicio 17
#palabras_usuario = input('Ingresa dos palabras: ')
#lista_usuario = palabras_usuario.split()
#print(lista_usuario[1] + ' ' + lista_usuario[0])

#ejercicio 17 manera 2
#palabras_usuario = input('Ingresa dos palabras: ')
#lista_usuario = palabras_usuario.split()
#lista_usuario.reverse()
#print(lista_usuario[0] + ' ' + lista_usuario[1])

#ejercicio 18
#datos_usuario_nombre = input('Ingresa tu nombre: ')
#datos_usuario_edad = input('Ingresa tu edad: ')
#datos_usuario_ciudad_residencia = input('Ingresa tu ciudad de residencia: ')
#print(f'Su nombre es {datos_usuario_nombre} tiene {datos_usuario_edad} años y vive en {datos_usuario_ciudad_residencia}')

#ejercicio 18 manera 2
#print(f'Nombre {input(Ingrese su nombre')},Edad:)...


#ejercicio 19
#numero = input('Ingrese un numero decimal: ')
#numeros_lista = numero.split('.')
#print(f'La parte entera es {numeros_lista[0]} y la parte decimal es {numeros_lista[1]}')
#Hacer de la otra manera restando la parte entera

#ejercicio 19 manera 2
# numero = float(input('Ingrese un numero decimal: '))
# numero_decimal = numero - int(numero)
# numero_entero = int(numero)
# print(f'La parte entera es {numero_entero} y la parte decimal es {numero_decimal}')
