# Import de biblioteca
import math
# CRIAR A FUNÇÃO AQUI:
k = math.pi
def funcao_a(n):
  return k / (math.factorial(n) + k)

# Import de biblioteca
import math
# CRIAR A FUNÇÃO AQUI:
k = math.pi
p = math.e
def funcao_b(n):
  return (k ** n - k) / (p * n)

# Declaração de variável
media_a = 0.00
media_b = 0.00
soma_a = 0.00
soma_b = 0.00
# MENU: REUSABILIDADE
try:
  # Menu
  print('Digite [1] para chamar a função A.')
  print('Digite [2] para chamar a função B.')
  print('Digite [0] para sair do programa.')
  # Entrada de dados
  opcao = int(input(''))
  # Tratamento de erro
  if opcao < 0 or opcao > 2:
    print('ERRO: dados de entrada.')
  else:
    # Fim do programa
      if opcao == 0:
        print('Fim do programa!')
      else:
        n = int(input('Informe o valor de n (Inteiro, maior ou igual a 0): '))
        if n < 0:
          print('n deve sero maior ou igual a 0.')
        else:
          if opcao == 1:
            for a in range(1, n + 1):
              termo_a = funcao_a(a)
              soma_a += termo_a
              print(f"f({a}) = {termo_a:.2f}")
            media_a = soma_a / n
            print(f"\nSoma dos termos da função A: {soma_a:.2f}")
            print(f"Média dos termos da função A: {media_a:.2f}")
          else:
            for b in range(1, n + 1):
              termo_b = funcao_b(b)
              soma_b += termo_b
              print(f"f({b}) = {termo_b:.2f}")
            media_b = soma_b / n
            print(f"Soma dos termos da função B: {soma_b:.2f}")
            print(f"Média dos termos da função B: {media_b:.2f}")
except Exception as erro:
  print(f"Erro de exceção: {erro}")
