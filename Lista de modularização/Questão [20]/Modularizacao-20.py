# CRIAR A FUNÇÃO AQUI:
def contracheque(salario_bruto, num_dependente):
  inss = salario_bruto * 0.11
  plano_saude = salario_bruto * 0.02
  vale_alimentacao = 1525 + (salario_bruto * 0.05) * num_dependente
  salario_liquido = salario_bruto - inss - plano_saude + vale_alimentacao
  total_descontos = inss + plano_saude
  return salario_liquido, total_descontos

# MENU: REUSABILIDADE
contador = 0 # Enumerar
while True:
  try:
    # Menu
    print('ESTE PROGRAMA CALCULA O SEU CONTRACHEQUE!')
    print('Digite [1] para calcular o contracheque.')
    print('Digite [0] para sair do programa.')
    opcao = int(input(''))
    # Tratamento de erro
    if opcao < 0 or opcao > 1:
      print('ERRO: dados de entrada')
    elif opcao == 0:
      print('Programa finalizado!')
      break # Quebra do código
    else:
      # Entrada de dados
      salario_bruto = float(input(f'{contador + 1}º Funcionário, informe seu salário bruto: '))
      # Tratamento de erro
      if salario_bruto < 0.00:
        print('ERRO: o salário deve ser acima de 0!')
      else:
        # Entrada de dados
        num_dependente = int(input('Informe quantos dependentes você tem (Esposa + filhos): '))
        # Tratamento de erro
        if num_dependente < 0:
          print('ERRO: dados de entrada!')
        else:
          contador += 1
          salario, desconto_total = contracheque(salario_bruto, num_dependente)
          # Resultado
          print(f'Seu salário liquido é de R${salario:.2f}, foi descontado dele R${desconto_total:.2f}.')
  except Exception as erro:
    print(f'ERRO DE EXCEÇÃO: {erro}')
