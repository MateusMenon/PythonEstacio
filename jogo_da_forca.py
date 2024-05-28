import random

def escolher_palavra():
  """
  Escolhe uma palavra aleatória da lista de palavras.
  """
  palavras = ['python', 'programação', 'tecnologia', 'desenvolvimento', 'algoritmo']
  return random.choice(palavras)

def exibir_forca(tentativas):
  """
  Exibe a forca na tela com base no número de tentativas restantes.

  """
  partes_forca = [
    """
      +---+
      |   |
      O   |
     /|\  |
     / \  |
            """,
    """
      +---+
      |   |
      O   |
     /|\  |
     /     |
            """,
    """
      +---+
      |   |
      O   |
     /|\  |
            """,
    """
      +---+
      |   |
      O   |
     /|   |
            """,
    """
      +---+
      |   |
      O   |
     /     |
            """,
    """
      +---+
      |   |
      O     |
            """,
  ]

  # Ajusta a lógica de exibição de acordo com as tentativas restantes
  if tentativas == 5:
    print(partes_forca[-1])  # Mostra o último item (parte completa)
  elif tentativas == 4:
    print(partes_forca[-2])  # Mostra o antipenúltimo item
  elif tentativas == 3:
      print(partes_forca[- 3])  #mostra o 3 de tras pra frente
  elif tentativas == 2:
      print(partes_forca[- 4])  #mostra o 4 de tras pra frente
  elif tentativas == 1:
      print(partes_forca[- 5])  #mostra o 5 de tras pra frente
  else:
    # Exibe todas as partes da forca até o limite de tentativas
    for i in range(len(partes_forca)):
      if i <= tentativas:
        print(partes_forca[i])
      else:
        break


def jogar():
  """
  Função principal do jogo da forca.
  """
  palavra_secreta = escolher_palavra()
  letras_usuario = []
  chances = 6

  while True:
    print("\n")
    for letra in palavra_secreta:
      if letra.lower() in letras_usuario:
        print(letra, end=" ")
      else:
        print("_", end=" ")
    print(f"\nVocê tem {chances} chances")

    tentativa = input("Escolha uma letra para adivinhar: ").lower()
    letras_usuario.append(tentativa)

    if tentativa not in palavra_secreta.lower():
      chances -= 1
      exibir_forca(chances)

    ganhou = True
    for letra in palavra_secreta:
      if letra.lower() not in letras_usuario:
        ganhou = False
        break

    if chances == 0 or ganhou:
      break

  if ganhou:
    print(f"\nParabéns, você ganhou! A palavra era: {palavra_secreta}")
  else:
    print(f"\nVocê perdeu! A palavra era: {palavra_secreta}")
    
  print('Obrigado por jogar com a gente!!!!!')

# Iniciar o jogo
jogar()
