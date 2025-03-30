# Declaração de variável
contador = 0
media = 0.00
numero = 0
numero_impar = 0
# Menu
print('Digite qualquer número ímpar e múltiplo de 7!')
while contador < 5:
  try:
    # Entrada de dados
    numero = int(input(''))
    # Tratamento de erro
    if numero < 7:
      print('ERRO: o número deve ser positivo e no mínimo 7!')
    else:
      if numero % 2 == 0 and numero % 7 != 0:
        print('O número deve ser ímpar e múltiplo de 7!')
      else: # Condição se o número é ímpar e múltiplo de 7
        contador += 1
        numero_impar += numero
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
# Cálculo de média
media = numero_impar / contador
# Resultado
print(f'A média dos números ímpares múltiplos de 7 é: {media:.2f}')
