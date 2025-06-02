# CRIAR / RESETAR LISTAS
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
      if len(cargo) < 3:
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

def LerPlano(plano):
  if plano == 1:
    return 1
  else:
    return 0

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
      print('Digite [1] se você possui um plano de saúde.')
      print('Digite [0] se você não possui um plano de saúde.')
      plano = int(input(''))
      if plano > 1 or plano < 0:
        print('ERRO: Digite apenas uma das duas opções apresentadas!')
      else:
        # INSERIR DADOS DO ALUNO:
        print(f'Entre com os dados do {len(empresa) + 1}º funcionário: ')
        nome = LerNome()
        cargo = LerCargo()
        mat = SortMat()
        plano_saude = LerPlano(plano)
        salario = LerSalario()
        # LISTA DE LISTAS:
        funcionarios = [nome, cargo, mat, plano_saude, salario]
        empresa.append(funcionarios)
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
    break

# Relatórios:
total_plano = [funcionarios for funcionarios in empresa if funcionarios[3] == 1]
percentual = (len(total_plano) / len(empresa)) * 100
print(f'Taxa de adesão ao plano de saúde: {percentual:.2f}%')

nome_plano = [funcionarios for funcionarios in empresa if funcionarios[3] == 1]
for valor in nome_plano:
  print(f'Nome dos funcionários que tem plano de saúde: {valor[0]}')

cargo_salario = [funcionarios[4] for funcionarios in empresa]
media_cargo = (sum(cargo_salario) / len(empresa))
for valor in empresa:
  if valor[4] > media_cargo: 
    print(f'{valor[0]} que está no cargo de {valor [1]}, ganha mais que a média.')

folha = [funcionarios[4] for funcionarios in empresa]
bruto = sum(folha)
liquido = bruto - (212.54 * len(total_plano))
print(f'Folha de pagamento Bruta (Sem desconto do(s) plano(s) de saúde): R${bruto: .2f}')
print(f'Folha de pagamento Líquida (Com desconto do(s) plano(s) de saúde): R${liquido: .2f}')
