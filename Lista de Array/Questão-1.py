import numpy as np

Arquivo: https://drive.google.com/file/d/1oSBBXrNH2waKvz06GLwMmjY0O4Og2WID/view

dataset1 = np.load('dataset1.npy')

''' Letra A)
Exibir na tela os 5 mais baixos e mais altos Salários dos Desenvolvedores em Salários Mínimos, sendo que:

um (1) Salário Mínimo = R$ 1.112,00.'''

salario_min = 1112.00
salarios_em_min = dataset1[:, 1] / salario_min
indices_ordenados = np.argsort(salarios_em_min)

print('\nDADOS DOS 5 DESENVOLVEDORES COM MENORES SALÁRIOS (em salários mínimos):\n')
for indice, valor in enumerate(indices_ordenados[:5]):
    funcionario = dataset1[valor]
    print(f'DESENVOLVEDOR {indice + 1}:')
    print(f'Matrícula       : {funcionario[0]: .0f}')
    print(f'Salário Bruto   : R$ {funcionario[1]:.2f}')
    print(f'Salário Mínimos : {funcionario[1] / salario_min:.2f}')
    print(f'Plano de Saúde  : {plano[int(funcionario[2])]}')
    print(f'Dependentes     : {funcionario[3]: .0f} Dependente(s)\n')

print('\nDADOS DOS 5 DESENVOLVEDORES COM MAIORES SALÁRIOS (em salários mínimos):\n')
for indice, valor in enumerate(indices_ordenados[-5:]):
    funcionario = dataset1[valor]
    print(f'DESENVOLVEDOR {indice + 1}:')
    print(f'Matrícula       : {funcionario[0]: .0f}')
    print(f'Salário Bruto   : R$ {funcionario[1]:.2f}')
    print(f'Salário Mínimos : {funcionario[1] / salario_min:.2f}')
    print(f'Plano de Saúde  : {plano[int(funcionario[2])]}')
    print(f'Dependentes     : {funcionario[3]: .0f} Dependente(s)\n')

''' Letra B)
A Amplitude Salarial = Maior Salário – Menor Salário, em Reais e em Salários Mínimos. Sabendo que o Salário Mínimo = R$ 1.112,00.'''

min_salario = min(dataset1[:, 1])
max_salario = max(dataset1[:, 1])
salario_min = 1112.00
amplitude_salarial = max_salario - min_salario
amplitude_salarial_em_min = amplitude_salarial / salario_min
print(f'Amplitude salarial em reais: R${amplitude_salarial: .2f}')
print(f'Amplitude salarial em salário(s) mínimo(s):{amplitude_salarial_em_min: .2f}')

''' Letra C)
A Média Salarial dos 100 Desenvolvedores Python com os maiores salários do estado.'''

salarios_ordem_desc = np.argsort(dataset1[:, 1][::-1][:100])
top_100 = dataset1[salarios_ordem_desc, 1]
media = np.mean(top_100)
print(f'A média dos 100 maiores salários de Desenvolver Python do Espírito Santo (ES): R${media: .2f}')

''' Letra D)
A folha de pagamento total desta empresa, sendo que cada funcionário terá:

Desconto: 2% do Salário Bruto, se o funcionário tiver plano de saúde.

Acréscimo: Vale Alimentação de 1% por dependente.'''

dependentes = dataset1[:, 3]
plano = dataset1[:, 2] == 1
bruto = sum(dataset1[:, 1])
desconto = np.where(plano, bruto * 0.02, 0)
acrescimo = 0.01 * dependentes * bruto
liquido = bruto - desconto + acrescimo
total = sum(liquido)
print(f'Folha de pagamento total desta empresa: R${total: .4f}')

''' Letra E)
Exibir na tela quanto (em R$) um aumento de 7% (para todos os desenvolvedores) injetará a mais na economia capixaba.'''

aumento = sum(dataset1[:, 1]) * 0.07
print(f'{aumento: .2f} reais será injetado, caso tenha um aumento de 7% nos salários de todos os desenvolvedores Python.')
