# CRIAR A FUNÇÃO AQUI:
def lerReajuste(opcao, preco, reajuste):
  if opcao == 1:
    return preco + ((preco * reajuste) / 100)
  else:
    return preco - ((preco * reajuste) / 100)

# MENU: REUSABILIDADE
contador = 0 # Enumerar
while contador < 3:
  # Tratamento de exceção
  try:
    # Entrada de dados
    preco = float(input(f'Informe o preço da {contador + 1}º mercadoria: '))
    opcao = float(input('Escolha o reajuste: [1] para Acréscimo ou [2] para Desconto. '))
    # Tratamento de erro
    if preco <= 0 or opcao < 1 or opcao > 2:
      print('ERRO: Dados de entrada')
    else:
      # Entrada de erro
      reajuste = float(input('Informe o reajuste do preco em (%):'))
      preco_final = lerReajuste(opcao, preco, reajuste)
      if opcao == 1:
        # Tratamento de erro
        if reajuste < 0:
          print('ERRO: o acréscimo deve ser maior ou igual a 0!')
        else:
          contador += 1
          # Resultado
          print(f'O preço com acréscimo da {contador}º mercadoria é: R${preco_final:.2f}')
      else:
        # Tratamento
        if reajuste > 100:
          print('ERRO: o desconto não pode passar de 100%!')
        else:
          contador += 1
          # Resultado
          print(f'O preço com desconto da {contador}º mercadoria é: R${preco_final:.2f}')
  except Exception as erro:
    print(f'ERRO DE EXCEÇÃO: {erro}')
