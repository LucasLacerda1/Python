# Declaração de variável
numero = 0
soma = 0

while True: # Loop
  try:  
    print('Informe o número de 10 a 90:')
    print('Digite [0] para encerrar o programa!')
    # Entrada de dados
    numero = int(input(''))
    if numero == 0:
      # Resultado
      print(f'A soma dos números lidos é: {soma}')
      break
    else:
      # Tratamento de erro
      if numero < 10 or numero > 90:
        print('ERRO: o número deve ser maior ou igual a 10 e menor ou igual a 90!')
      elif numero % 5 == 2: # Verificação se o número divido por 5 da resto 2
        soma += numero # Soma dos números após a verificação
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
