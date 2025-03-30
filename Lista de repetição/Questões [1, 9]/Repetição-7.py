# Declaração de variável
impar = 0
quantidade = 0
try:
  for contador in range (9, 91): # Percorre os números entre [9, 90]
    if contador % 2 != 0 and contador % 3 == 0 and contador % 5 != 0: # Verificação se o número é ímpar múltiplo de 3 e não múltiplo de 5
      impar += contador
      quantidade += 1
      print(f'{quantidade}º número: {contador}')
  # Resultado final
  print(f'A soma dos números ímpares múltiplos de 3 e não múltiplos de 5 compreendidos entre [9, 90]: {impar}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
