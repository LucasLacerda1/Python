# CRIAR A FUNÇÃO AQUI:
def lerNumero(numero, opcao):
  '''
  HELP: GUI - lerNumero (INT):
  - TRATAMENTO DE ERRO
  - TRATAMENTO DE EXCEÇÃO
  - NÚMERO MÍNIMO: 1
  '''
  par = 1
  impar = 1
  while True:
    # Tratamento de exceção
    try:
        if opcao == 0:
          for contador in range (1, numero + 1):
            if contador % 2 == 0:
              par *= contador
          return par
        elif opcao == 1:
          for contador in range (1, numero + 1):
            if contador % 2 != 0:
              impar *= contador
          return impar
    except Exception as erro:
        print(f'ERRO DE EXCEÇÃO: {erro}')

# MENU: REUSABILIDADE
contador = 0  # Enumerar
while contador < 5:
  try:
    # Menu
    print('Escolha se você quer retornar a multiplicação dos números pares ou ímpares.')
    print('Digite [0] para par.')
    print('Digite [1] para ímpar.')
    # Entrada de dados
    opcao = int(input())
    if opcao < 0 or opcao > 1:
        print('ERRO: ENTRADA DE DADOS.')
    else:
        numero = int(input('Informe um número inteiro maior que 1:'))
        if numero < 1:
          print('ERRO NO NÚMERO: TENTE DE NOVO.')
        else:
          contador += 1
          if opcao == 0:
              mult_par = lerNumero(numero, 0)
              print(f'A multiplicação dos números pares é: {mult_par}')
          else:
              mult_impar = lerNumero(numero, 1)
              print(f'A multiplicação dos números ímpares é: {mult_impar}')
  except Exception as erro:
    print(f'ERRO DE EXCEÇÃO: {erro}')
