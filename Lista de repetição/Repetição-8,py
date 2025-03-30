# Declaração de variável
contador = 0
mix_1 = 0
mix_2 = 0
mix_3 = 0

# Menu
print('==============================================')
print('       Qual mix de sabor você gostou?        ')
print(' Digite [1] caso você tenha gostado do Mix 1.')
print(' Digite [2] caso você tenha gostado do Mix 2.')
print(' Digite [3] caso você tenha gostado do Mix 3.')
print(' Digite [0] para sair do programa.')
print('==============================================')

while True:
  try:
    contador += 1
    # Entrada de dados
    opcao = int(input(f'{contador}° Cliente, sua opção é: '))
    if opcao == 0:  # Quebra do programa
      # Cálculo das porcentagens
      if contador > 0:
        porcentagem_mix_1 = (mix_1 / contador) * 100
        porcentagem_mix_2 = (mix_2 / contador) * 100
        porcentagem_mix_3 = (mix_3 / contador) * 100
      # Resultados
      if mix_1 > 0:
        print(f'{porcentagem_mix_1:.1f}% dos clientes gostaram do Mix 1.')
      if mix_2 > 0:
        print(f'{porcentagem_mix_2:.1f}% dos clientes gostaram do Mix 2.')
      if mix_3 > 0:
        print(f'{porcentagem_mix_3:.1f}% dos clientes gostaram do Mix 3.')
      break
      # Tratamento de erro
    elif opcao < 1 or opcao > 3:
      print('ERRO: Escolha uma das 4 opções')
    elif opcao == 1:  # Contagem de clientes que preferem Mix 1
      mix_1 += 1
    elif opcao == 2:  # Contagem de clientes que preferem Mix 2
      mix_2 += 1
    elif opcao == 3:  # Contagem de clientes que preferem Mix 3
       mix_3 += 1
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
