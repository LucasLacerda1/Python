# CRIAR / RESETAR LISTAS
import numpy

funcionarios = []
empresa = []

# MODULARIZAR DADOS DE LEITURA: ?
def lerNome():
  while True:
    try:
      nome = input('\nInforme seu nome: ')
      if len(nome) < 3:
        print('\nERRO: Informe novamente.')
      else:
        break
    except:
      print('\nERRO: Informe novamente.')
  return nome

def lerCargo():
  while True:
    try:
      cargo = input('\nInforme seu cargo: ')
      if len(cargo) < 3:
        print('\nERRO: Informe novamente.')
      else:
        break
    except:
      print('\nERRO: Informe novamente.')
  return cargo

def sortMat():
  std = 1000
  mean = 10000
  size = 1
  valid_mat = [valor[1] for valor in empresa]
  while True:
    mat = int(numpy.random.normal(mean, std, size))
    if 0 < mat < 10000 and mat not in valid_mat:
      return mat

def lerPlano(plano):
  if plano == 1:
    return 1
  else:
    return 0

def lerSalario():
  while True:
    try:
      salario = float(input('\nInforme seu salário em R$: '))
      if salario < 1512.00:
        print('\nERRO: Informe novamente.')
      else:
        break
    except:
      print('\nERRO: Informe novamente.')
  return salario

def report_1():
  total_plano = [funcionarios for funcionarios in empresa if funcionarios[3] == 1]
  percentual = (len(total_plano) / len(empresa)) * 100
  return percentual, total_plano

def report_2():
  nome_plano = [funcionarios for funcionarios in empresa if funcionarios[3] == 1]
  return nome_plano

def report_3():
  cargo_salario = [funcionarios[4] for funcionarios in empresa]
  media_cargo = (sum(cargo_salario) / len(empresa))
  return media_cargo

def report_4():
  folha = [funcionarios[4] for funcionarios in empresa]
  total_plano = [funcionarios for funcionarios in empresa if funcionarios[3] == 1]
  bruto = sum(folha)
  liquido = bruto - (212.54 * len(total_plano))
  return bruto, liquido

# MENU: PROGRAMA PRINCIPAL (MAIN)
contador = 0 # Enumerar
while contador < 100:
  try:
    print('\nMenu')
    print('1. Registrar funcionário.')
    print('2. Exibir taxa de adesão ao plano de saúde.')
    print('3. Exibir nomes dos funcionários que possuem plano de saúde.')
    print('4. Exibir cargos dos funcionários que estão acima da média salarial.')
    print('5. Exibir total da folha de pagamento: Bruto e Líquido.')
    print('Qualquer tecla: Sair.') 
    opcao = int(input('Sua opção: '))
    if opcao == 1:
      print('\nDigite [1] se você possui um plano de saúde.')
      print('Digite [0] se você não possui um plano de saúde.')
      plano = int(input(''))
      if plano > 1 or plano < 0:
        print('ERRO: Digite apenas uma das duas opções apresentadas!')
      else:
        # INSERIR DADOS DO ALUNO:
        print(f'\nEntre com os dados do {len(empresa) + 1}º funcionário: ')
        nome = lerNome()
        cargo = lerCargo()
        mat = sortMat()
        plano_saude = lerPlano(plano)
        salario = lerSalario()
        # LISTA DE LISTAS:
        funcionarios = [nome, cargo, mat, plano_saude, salario]
        empresa.append(funcionarios)
        contador += 1
    elif opcao == 2:
      percentual, total_plano = report_1()
      if len(total_plano) == 0:
        print('\nNão há funcionários com plano de saúde!')
      else:
        print(f'\nTaxa de adesão ao plano de saúde: {percentual:.2f}%')
    elif opcao ==3:
      nome_plano = report_2()
      if len(nome_plano) == 0:
        print('\nNão há funcionários cadastrados!')
      else:
        for valor in nome_plano:
          print(f'\nNome dos funcionários que tem plano de saúde: {valor[0]}')
    elif opcao == 4:
      if len(empresa) == 0:
        print('\nNão há funcionários cadastrados!')
      else:
        media_cargo = report_3()
        for valor in empresa:
          if valor[4] > media_cargo: 
            print(f'{valor[0]} que está no cargo de {valor [1]}, ganha mais que a média.')
    elif opcao == 5:
      bruto, liquido = report_4()
      if len(empresa) == 0:
        print('\nNão há funcionários cadastrados!')
      elif liquido == bruto:
        print('\nNão há funcionários com plano de saúde!')
      else:
        print(f'\nFolha de pagamento Bruta (Sem desconto do(s) plano(s) de saúde): R${bruto: .2f}')
        print(f'Folha de pagamento Líquida (Com desconto do(s) plano(s) de saúde): R${liquido: .2f}')
    else:
      print('FIM DO PROGRAMA')
      break
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
    break
