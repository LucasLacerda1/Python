# Declaração de variável
contador = 0
desemp = 0
emp = 0
pDesemp = 0.0
pEmp = 0.0

while contador < 10000:
  try:
    contador += 1
    print(f'Digite [0] se o habitante está desempregado')
    print(f'Digite [1] se o habitante está empregado:')
    # Dados de entrada
    habitantes = int(input(''))
    # Tratamento de erro
    if habitantes < 0 or habitantes > 1:
      print('ERRO: dados de entrada')
    else:
      if habitantes == 0:   # Contagem de desempregados
        desemp += 1
      else:  # Contagem de empregados
        emp += 1
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
pDesemp = (desemp / contador) * 100 # Cálculo da porcentagem de desempregados
pEmp = (emp / contador) * 100 # Cálculo da porcentagem de empregados
# Resultados
print(f'A porcentagem de desempregados em relação ao número de habitantes é: {pDesemp:.1f}%')
print(f'A porcentagem de empregados em relação ao número de habitantes é: {pEmp:.1f}%')
