import numpy

funcionarios = []
empresa = []

# MODULARIZAR DADOS DE LEITURA: ?
def LerNome():
  while True:
    try:
      nome = input('Informe seu nome: ')
      if len(nome) < 3:
        print('ERRO: Informe novamente.')
      else:
        break
    except:
      print('ERRO: Informe novamente.')
  return nome

def LerCargo():
  while True:
    try:
      cargo = input('Informe seu cargo: ')
      if len(cargo < 3):
        print('ERRO: Informe novamente.')
      else:
        break
    except:
      print('ERRO: Informe novamente.')
  return cargo

def SortMat():
  std = 1000
  mean = 10000
  size = 1
  mat = [valor for valor in (numpy.random.normal(mean, std, size))]
  return mat

def LerPlano():
  while True:
    try:
      opcao = int(input('Digite [1] se você possui plano de saúde, digite [2] se você não possui: '))
      if opcao < 1 or opcao > 2:
        print('ERRO: Informe novamente.')
      else:
        if opcao == 1:
          plano = 'Possui plano'
          break
        else:
          plano = 'Não possui plano'
          break
    except:
      print('ERRO: Informe novamente.')
  return plano

def LerSalario():
  while True:
    try:
      salario = float(input('Informe seu salário em R$: '))
      if salario < 1512.00:
        print('ERRO: Informe novamente.')
      else:
        break
    except:
      print('ERRO: Informe novamente.')
  return salario

# MENU: PROGRAMA PRINCIPAL (MAIN)
print('Menu')
print('OPÇÃO 0: Registrar funcionário.')
print('Qualquer teclas: Sair.')
while True:
  try:
    opcao = int(input('SUA OPÇÃO: '))
    if(opcao != 0):
      print('FIM DO PROGRAMA')
      break
    else:
      # INSERIR DADOS DO ALUNO:
      print(f'Entre com os dados do {len(empresa) + 1}º funcionário: ')
      nome = LerNome()
      mat = SortMat()
      plano = LerPlano()
      salario = LerSalario()
      # LISTA DE LISTAS:
      funcionarios = [nome, mat, plano, salario]
      empresa.append(funcionarios)
      print('Funcionário cadastrado com sucesso.')
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
    break
