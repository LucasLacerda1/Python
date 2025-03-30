# Declaração de variável
cartao = 0 # Enumerar
cartao_standard = 0
cartao_vip = 0
cliente = 0 # Enumerar
opcao = 0
porcentagem_cartao_standard = 0.00
porcentagem_cartao_vip = 0.00
salario = 0.00
# Loop
while True:
  try:
    # Menu
    print('Digite [1] para cadastrar um cliente!')
    print('Digite [0] para sair do programa!')
    # Entrada de dados
    opcao = int(input(''))
    #Tratamento de erro
    if opcao < 0 or opcao > 1:
      print('ERRO: digite [1] ou [0] no programa!')
    # Fim do programa
    elif opcao == 0:
      # Resultado
      if cartao_standard > 0:
        porcentagem_cartao_standard = (cartao_standard / cartao) * 100 # Cálculo de porcentagem dos cliente que possui cartão standard
        print(f'{porcentagem_cartao_standard}% dos clientes possui cartão standard!')
      if cartao_vip > 0:
        porcentagem_cartao_vip = (cartao_vip / cartao) * 100 # Cálculo de porcentagem dos cliente que possui cartão vip
        print(f'{porcentagem_cartao_vip}% dos clientes possui cartão vip!')
      if cartao == 0:
        print('Não houve clientes cadatrados!')
      print('Fim do programa!')
      break # Quebra do cógido
    else:
      # Entrada de dados
      salario = float(input(f'Informe seu salário do {cliente + 1}º cliente: '))
      if salario < 0:
        print('ERRO: dados de entrada')
      elif salario >= 5000.00:
        cartao += 1
        cartao_vip += 1
        cliente += 1
      else:
        cartao += 1
        cartao_standard += 1
        cliente += 1
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
