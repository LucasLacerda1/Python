# Import de biblioteca
import numpy as np
# declaração de variável
contador = 0
maior_numero = -1
menor_numero = np.inf
numero = 0
# Menu
print('Digite qualquer número positvo inteiro!')
while True:
  try:
    # Entrada de dados
    numero = int(input(''))
    if numero < 0:
      print('ERRO: o número deve ser positivo e maior que zero!')
    elif numero == 0:
      print('Fim do programa!')
      break # Quebra do cógido
    else:
      if numero < menor_numero: # Verificação do menor número
        menor_numero = numero
      if numero > maior_numero: # Verificação do maior número
          maior_numero = numero
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
# Resultado
print(f'O menor número  é: {menor_numero}')
print(f'O maior número  é: {maior_numero}')
