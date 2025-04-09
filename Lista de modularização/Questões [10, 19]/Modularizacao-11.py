# CRIAR A FUNÇÃO AQUI:
def calculo(ano, num):
  if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    return 0, ano // num, ano % num
  else:
    return 1, ano // num, ano % num

# MENU: REUSABILIDADE
try:
  # Entrada de dados
  ano = int(input('Informe um ano qualquer (maior que 0): '))
  print('Digite [0] para sair do programa!')
  # Tratamento de erro
  if ano < 0:
    print('ERRO: informe um ano acima de 0!')
  else:
    # Menu
    print('Escolha um desses três números:')
    print('. 4')
    print('. 100')
    print('. 400')
    # Entrada de dados
    num = int(input(''))
    # Tratamento de erro
    if num != 4 and num != 100 and num != 400:
      print('ERRO: informe um dos três números apresentados')
    else:
      bissexto, quociente, resto = calculo(ano, num)
      # Resultados
      if bissexto == 0:
        print(f'O ano {ano} é bissexto.')
      else:
        print(f'O ano {ano} não é bissexto.')
      print(f'O quociente da divisão do ano {ano} pelo número escolhido {num} é: {quociente:.2f}')
      print(f'O resto da divisão do ano {ano} pelo número escolhido {num} é: {resto:.2f}')
except Exception as erro:
  print(f'ERRO: {erro}')
