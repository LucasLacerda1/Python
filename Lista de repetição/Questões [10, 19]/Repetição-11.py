# Declaração de variável
contador = 0
quantidade = 0
numero = 0
try:
  print('Informe um número inteiro: ')
  # Dados de entrada
  numero = int(input(''))
  for contador in range (numero + 1, 50 + numero + 1): # Conta os 50 números subsequentes do número informado
    quantidade += 1 # Contagem
    # Resultado
    print(f'{quantidade}º número: {contador}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
