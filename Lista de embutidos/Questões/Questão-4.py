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
  total = [valor[2] for valor in banco]
  max_Total = max(total)
  max_Indice = total.index(max_total)
  return max_Indice

# MENU: PROGRAMA PRINCIPAL (MAIN)
while True:
    try:
      print('\n Menu')
      print('1. Registrar correntista')
      menu = int(input(''))
      if menu == 1:
        print(f'Entre com os dados do {len(banco) + 1}º correntista: ')
        nome = LerNome()
        conta = LerConta()
        extrato = LerExtrato
        correntista = [nome, conta, extrato]
        banco.append(correntista)
      elif menu == 2:
        if len(banco) == 0:
          print('ERRO: Não há correntista registrados!')
        else:
          Report_1 = Report_1()
          print('\n Correntista com a maior mavimentação do ano.')
          print(f'Nome do correntista: {banco[max_Indece[0]]}')
          print(f'Movimentação anual: {banco[max_Indece[1]]}')
    except Exception as ERRO:
      print(f'ERRO: {ERRO}')
