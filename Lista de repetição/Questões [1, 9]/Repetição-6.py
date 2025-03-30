# Declaração de variável
contador = 0
classe_A = 0
classe_B = 0
classe_C = 0
salario_minimo = float(998.05)

while contador < 8:
  try:
    contador += 1
    print(f'Digite o seu salário (MÍNIMO: R$ 998.05):')
    # Dados de entrada
    salario = float(input(''))
    # Tratamento de erro
    if salario < salario_minimo:
      print('ERRO: insira um valor maior que R$ 998.05')
    else:
      if salario >= salario_minimo * 15: # Contagem de clientes pertencentes à classe A
        classe_A += 1
      elif salario >= salario_minimo * 5: # Contagem de clientes pertencentes à classe B
        classe_B += 1
      else: # Contagem de clientes pertencentes à classe C
        classe_C += 1
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
porcentagem_A = (classe_A / contador) * 100 # Cálculo da porcentagem de clientes pertencentes à classe A
porcentagem_B = (classe_B / contador) * 100 # Cálculo da porcentagem de clientes pertencentes à classe B
porcentagem_C = (classe_C / contador) * 100 # Cálculo da porcentagem de clientes pertencentes à classe C
# Resultados
print(f'{porcentagem_A:.1f}% dos clientes pertencem à A.')
print(f'{porcentagem_B:.1f}% dos clientes pertencem à B.')
print(f'{porcentagem_C:.1f}% dos clientes pertencem à C.')
