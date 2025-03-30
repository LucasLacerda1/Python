# Declaração de variável
contador = 0 # Enumerar
contador_escolaridade_fundamental = 0 # Enumerar
contador_escolaridade_medio = 0 # Enumerar
contador_escolaridade_superior = 0 # Enumerar
escolaridade = 0
escolaridade_fundamental = 0
escolaridade_medio = 0
escolaridade_superior = 0
media_escolaridade_fundamental = 0.0
media_escolaridade_medio = 0.0
media_escolaridade_superior = 0
salario = 0.0
while contador < 6: # loop
  try:
    # Entrada de dados
    print('Digite [0] caso sua escolaridade seja ensino fundamental!')
    print('Digite [1] caso sua escolaridade seja ensino médio!')
    print('Digite [2] caso sua escolaridade seja ensino superior!')
    escolaridade = int(input(''))
    salario = float(input('Informe seu salário: '))
    # Tratamento de erro
    if escolaridade < 0 or escolaridade > 2 or salario < 0:
      print('ERRO: dados de entrada!')
    else:
      contador += 1
      if escolaridade == 0:
        contador_escolaridade_fundamental += 1
        media_escolaridade_fundamental += salario
      elif escolaridade == 1:
        contador_escolaridade_medio += 1
        media_escolaridade_medio += salario
      else:
        contador_escolaridade_superior += 1
        media_escolaridade_superior += salario
  except Exception as ERRO_EXCECAO:
    print(f'ERRO: {ERRO_EXCECAO}')
# Resultado
if contador_escolaridade_fundamental > 0:
  media_escolaridade_fundamental /= contador_escolaridade_fundamental
  print(f'A média salarial de quem tem a escolaridade de ensino fundamental é: R$ {media_escolaridade_fundamental:.2f}')
if contador_escolaridade_medio > 0:
  media_escolaridade_medio /= contador_escolaridade_medio
  print(f'A média salarial de quem tem a escolaridade de ensino médio é: R$ {media_escolaridade_medio:.2f}')
if contador_escolaridade_superior > 0:
  media_escolaridade_superior /= contador_escolaridade_superior
  print(f'A média salarial de quem tem a escolaridade de ensino superior é: R$ {media_escolaridade_superior:.2f}')
