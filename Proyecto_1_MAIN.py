import random
import os

def limpiar_pantalla():
  os.system("cls")

def iniciar_juego():
  grafico = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
    # Lista de palabras predefinidas
  palabras = ["casa", "vaso" , "valija" , "computadora" , "lampara" , "alfajor" , "informatorio"]

  #Definiendo variables
  palabra_secreta = random.choice(palabras)
  palabra_actual = "_" * len(palabra_secreta)
  letras_adivinadas = []
  intentos_restantes = 6 #Numero maximo de intentos

  
  for letras in palabra_actual:
    print(letras, end= " ")

  while True:
    
    print(grafico[intentos_restantes])
    letra_ingresada = input("Ingrese una letra: ").lower()
    if set(letra_ingresada) == set(palabra_secreta):
      print("¡Has acertado la palabra!")
      break
  
  
    if len(letra_ingresada) != 1 or not letra_ingresada.isalpha():
      print("Por favor, ingresa una sola letra válida.")
      print(f" Palabra actual: \n {palabra_actual}")
      continue
  
  
    if letra_ingresada in letras_adivinadas:
      print("Ya has adivinado esa letra antes.")
      continue
  
  
    if letra_ingresada in palabra_secreta:
      letras_adivinadas.append(letra_ingresada)
      print("¡Adivinaste una letra!")
    else:
      intentos_restantes -= 1
      print(f"Letra incorrecta. Te quedan {intentos_restantes} intentos.")
  
  
    palabra_actual = ''.join([" " + letra_ingresada if letra_ingresada in letras_adivinadas else ' _' for letra_ingresada in palabra_secreta])
    print(f"Palabra actual: \n {palabra_actual}")
    
    if palabra_actual == palabra_secreta:
      print("¡Has ganado! La palabra secreta es:", palabra_secreta)
      break
    
    if intentos_restantes == 0:
      print("¡Perdiste! La palabra secreta era:", palabra_secreta)

# Iniciar el juego
nombre_jugador = input("¿Como es tu nombre? ")

if __name__ == "__main__":
    print(f"¡Hola, {nombre_jugador}. Bienvenido al juego del Ahorcado !")
    iniciar_juego()
