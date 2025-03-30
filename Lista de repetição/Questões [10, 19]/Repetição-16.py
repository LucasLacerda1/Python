# Import de biblioteca
import numpy as np
# declaração de variável
contador = 0
maior_impar = -1
menor_impar = np.inf
maior_par = -1
menor_par = np.inf
numero = 0
# Menu
print('Digite qualquer número positvo inteiro!')
while contador < 10:
  try:
    numero = int(input(''))
    if numero <= 0:
      print('ERRO: o número deve ser positivo e maior que zero!')
    else:
      if numero % 2 == 0:
        contador += 1
        if numero > maior_par:
          maior_par = numero
        if numero < menor_par:
          menor_par = numero
      elif numero % 2 != 0:
        contador += 1
        if numero > maior_impar:
          maior_impar = numero
        if numero < menor_impar:
          menor_impar = numero
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
print(f'O maior número par é: {maior_par}')
print(f'O menor número par é: {menor_par}')
print(f'O maior número ímpar é: {maior_impar}')
print(f'O menor número ímpar é: {menor_impar}')
