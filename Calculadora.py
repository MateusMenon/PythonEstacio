def somar(x, y):
  return x + y

def subtrair(x, y):
  return x - y

def multiplicar(x, y):
  return x * y

def dividir(x, y):
  if y == 0:
    raise ZeroDivisionError("Não é possível dividir por zero.")
  return x / y

while True:
  print("\n--- Calculadora Digital ---")
  print("1. Somar")
  print("2. Subtrair")
  print("3. Multiplicar")
  print("4. Dividir")
  print("5. Sair")

  opcao = int(input("Digite sua opção: "))

  if opcao == 1:
    try:
      x = float(input("Digite o primeiro número: "))
      y = float(input("Digite o segundo número: "))
      resultado = somar(x, y)
      print(f"Soma: {resultado}")
    except ValueError:
      print("Entrada inválida. Digite números válidos.")
  elif opcao == 2:
    try:
      x = float(input("Digite o primeiro número: "))
      y = float(input("Digite o segundo número: "))
      resultado = subtrair(x, y)
      print(f"Subtração: {resultado}")
    except ValueError:
      print("Entrada inválida. Digite números válidos.")
  elif opcao == 3:
    try:
      x = float(input("Digite o primeiro número: "))
      y = float(input("Digite o segundo número: "))
      resultado = multiplicar(x, y)
      print(f"Multiplicação: {resultado}")
    except ValueError:
      print("Entrada inválida. Digite números válidos.")
  elif opcao == 4:
    try:
      x = float(input("Digite o primeiro número: "))
      y = float(input("Digite o segundo número: "))
      resultado = dividir(x, y)
      print(f"Divisão: {resultado}")
    except ZeroDivisionError as e:
      print(f"Erro: {e}")
    except ValueError:
      print("Entrada inválida. Digite números válidos.")
  elif opcao == 5:
    print("Saindo da calculadora...")
    break
  else:
    print("Opção inválida. Tente novamente.")
