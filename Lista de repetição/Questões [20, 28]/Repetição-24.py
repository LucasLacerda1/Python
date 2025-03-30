# Declaração de variável
contador = 0 # Enumerar
reajuste = 0
valor_total = 0.00
while (contador < 50):
  try:
    # Entrada de dados
    preco = float(input('Informe o valor da mercadoria em reais: '))
    # Tratamento de erro
    if (preco <= 0):
      print('ERRO: dados de entrada')
    else:
      contador += 1
      valor_total += preco
      reajuste = valor_total - (valor_total * 0.05)
      if (reajuste > 25.50):
        reajuste = reajuste + (reajuste * 0.02)
  except Exception as ERRO_EXCECAO:
    print(f'ERRO: {ERRO_EXCECAO}')
# Resultado
print(f'O valor total ser pago é: R${reajuste:.2f}')
