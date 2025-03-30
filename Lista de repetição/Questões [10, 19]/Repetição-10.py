# Declaração de variável
contador = 0
media = 0
numero = 0
quantidade = 0
soma = 0
try:
  print('Informe um número inteiro, positivo e maior ou igual a 1: ')
  # Dados de entrada
  numero = int(input(''))
  # Tratamento de erro
  if numero < 1:
    print('ERRO: o número deve ser inteiro, positivo e maior ou igual a 1!')
  else:
    for contador in range (6, 6 * numero + 1): # Conta os número no intervalo de [6, 6 * número]
      if contador % 6 == 0: # Veirificação se o número é múltiplo de 6
        quantidade += 1
        soma += contador # Soma dos números após a verificação
    media = soma / quantidade # Média das soma dos números múltiplos de 6
    # Resultado
    print(f'A média dos números múltiplos de 6 no intervalo de [6, 6 * número] é: {media:.1f}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
