# Declaração de variável
media_negativo = 0.0
media_positivo = 0.0
negativo = 0 # Enumerar
numero = 0.0
positivo = 0 # Enumerar
soma_negativo = 0.0
soma_positivo = 0.0
while True: # Loop
  try:
    # Menu
    print('Digite um número positivo ou negativo.')
    print('Digite [0] para encerrar o programa!')
    # Entrada de dados
    numero = float(input(''))
    if numero == 0:
      if negativo > 0:
        media_negativo = soma_negativo / negativo
        # Resultado
        print(f'A média dos números negativos lidos é: {media_negativo:.2f}')
      else:
        print('Não foi informado nenhum número negativo!')
      if positivo > 0:
        media_positivo = soma_positivo / positivo
        # Resultado
        print(f'A média dos números positivos lidos é: {media_positivo:.2f}')
      else:
        print('Não foi informado nenhum número positivo!')
      print('FIM DO PROGRAMA!')
      break # Quebra do loop
    else:
      if numero > 0:
        positivo += 1
        soma_positivo += numero # Soma dos números positivos
      else:
        negativo += 1
        soma_negativo += numero # Soma dos números negativos
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
