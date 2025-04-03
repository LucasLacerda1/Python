# CRIAR A FUNÇÃO AQUI:
def lerPreco(preco, reajuste):
   return preco + ((preco * reajuste) / 100)

# MENU: REUSABILIDADE
contador = 0 # Enumerar
while contador < 3:
  try:
    # Entrada de dados
    preco = float(input('Informe o preço da mercadoria: '))
    reajuste = float(input('Informe o reajuste do preco em (%):'))
    # Tratamento de erro
    if preco <= 0 or reajuste < 0:
      print('ERRO: Dados de entrada')
    else:
      contador += 1
      preco_final = lerPreco(preco, reajuste)
      print(f'O preço reajustado da {contador}º mercadoria é: R${preco_final:.2f}')
  except Exception as erro:
    print(f'ERRO DE EXCEÇÃO: {erro}')
