# Declaraçaõ de variável
contador = 0
negativo = 0
numero = 0.0
positivo = 0
porcentagem_positivo = 0.0
porcentagem_negativo = 0.0
# Menu
print('Digite qualquer número dentre os reais, exceto 0!')
print('Caso queira parar o programa, digite [0]!')
while True:
  try:
    numero = float(input(''))
    if numero > 0:
      contador += 1
      positivo += 1
    elif numero < 0:
      contador += 1
      negativo += 1
    else:
      if positivo > 0:
        porcentagem_positivo = (positivo / contador) * 100
        print(f'{porcentagem_positivo}% foram números postivos!')
      if negativo > 0:
        porcentagem_negativo = (negativo / contador) * 100
        print(f'{porcentagem_negativo}% foram números negativos!')
      break
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
