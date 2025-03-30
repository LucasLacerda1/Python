# Import de biblioteca
import math
# Declaração de variável
contador = 0 # Enumerar
media = 0.00
numero = 0.00
soma = 0.00
# Menu
print('Digite um número presente no intervalo de [10 * π3, 100 * π]!')
while True:
  try:
    # Entrada de dados
    numero = float(input(''))
    # Fim do programa
    if numero < (10 * (math.pi ** 3)) or numero > (100 * math.pi ):
      print('Fim do programa!')
      # Cálculo de média
      if contador > 0:
        media = soma / contador
        # Resultado
        print(f'A média dos números presentes no intervalo é: {media:.2f}') 
      else:
        print('Nenhum número válido foi inserido!')
      break # Quebra de código
    else:
      contador += 1
      soma += numero
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
