# Declaração de variável
contador = 0
quantidade = 0 # Enumerador

print('Esse programa irá mostras todos os múltiplos de 7 ou 13 no intervalo de [1000, 1500]')
try:
  for contador in range (1000, 1501):
    if contador % 7 == 0 or contador % 7 == 0: # Verificação se o contador é múltiplo de 7 ou 13
      quantidade += 1
      # Resultado
      print(f'{quantidade}º número: {contador}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
