import numpy

# CRIAR / RESETAR LISTAS
banco = []
correntista = []
extrato = []

# MODULARIZAR DADOS DE LEITURA: ?
def LerNome():
  while True:
    try:
      nome = input('Informe seu nome: ')
      if len(nome) < 3:
        print('ERRO: Informe o seu nome novamente.')
      else:
        break
    except:
      print('ERRO: Informe o seu nome novamente.')
  return nome

def LerConta():
  while True:
    try:
      conta = int(input('Informe o número da conta de 1 a 99.999: '))
      if conta < 1 or conta > 99999:
        print('ERRO: Informe o número da conta novamente (1 a 99.999)!!')
      else:
        break
    except:
      print('ERRO: Informe o número da conta novamente (1 a 99.999)!!')
  return conta

def LerExtrato():
  mean = 5000.01
  std = 505.01
  size = 12 # meses
  extrato = [valor for valor in (numpy.random.normal(mean, std, size))]
  return extrato

def Report_1():
  total = [sum(valor[2]) for valor in banco]
  max_Total = max(total)
  max_Indice = total.index(max_Total)
  return max_Indice

def Report_2():
  while True:
    try:
      print('\nMenu')
      print('Digite o número da conta do correntista que você deseja.')
      for valor in banco:
        print(f'A conta de número {valor[1]} pertence ao/a {valor[0]}')
      corrent_account = int(input('Número da conta (1 a 99.999): '))
      if corrent_account < 1 or corrent_account > 99999:
        print('ERRO: Informe o número da conta novamente (1 a 99.999)!!')
      else:
        lista_contas = [valor[1] for valor in banco]
        indice = lista_contas.index(corrent_account)
        break
    except :
      print(f'ERRO: a conta com o número {corrent_account}!')
  return indice

def Report_3():
  try:
    anual_finance = [sum(valor[2]) for valor in banco]
  except:
    print('Não há correntistas cadatrados')
  return sum(anual_finance)

# MENU: PROGRAMA PRINCIPAL (MAIN)
while True:
    try:
      print('\n Menu')
      print('1. Registrar correntista.')
      print('2. Correntista com a maior movimentação anual de extrato.')
      print('3. Movimentação financeira total trimestral de acordo com a conta.')
      print('4. Relatório financeiro da movimentação anual de todos os correntistas juntos.')
      print('5. Lucro dos acionistas.')
      print('Qualquer teclas: Sair.')
      menu = int(input(''))
      if menu == 1:
        print(f'Entre com os dados do {len(banco) + 1}º correntista: ')
        nome = LerNome()
        conta = LerConta()
        extrato = LerExtrato()
        correntista = [nome, conta, extrato]
        banco.append(correntista)
      elif menu == 2:
        if len(banco) == 0:
          print('ERRO: Não há correntista registrados!')
        else:
          max_Indice = Report_1()
          print('\n Correntista com a maior movimentação do ano.')
          print(f'Nome do correntista: {banco[max_Indice][0]}')
          print(f'Número da conta: {banco[max_Indice][1]}')
      elif menu == 3:
        indice = Report_2()
        print(f'Movimentação do 1º trimestre: R${sum(banco[indice][2][0:3]): .2f}')
        print(f'Movimentação do 2º trimestre: R${sum(banco[indice][2][3:6]): .2f}')
        print(f'Movimentação do 3º trimestre: R${sum(banco[indice][2][6:9]): .2f}')
        print(f'Movimentação do 4º trimestre: R${sum(banco[indice][2][9:12]): .2f}')
      elif menu == 4: 
        anual_finance = Report_3()
        print(f'Movimentação Anual acumulada de todos os correntistas: R${anual_finance:.2f}')
      elif menu == 5:
        anual_finance = Report_3()
        print(f'Lucro total do acionistas: R${anual_finance * 0.07:.2f}')
      else:
        print('Fim do programa')
        break
    except Exception as ERRO:
      print(f'ERRO: {ERRO}')
