# Declaração de variável
altura_feminina = 0.00
altura_masculina = 0.00
altura_media_feminina = 0.00
altura_media_masculina = 0.00
contador = 0
sexo = 0
sexo_feminino = 0
sexo_masculino = 0

while contador < 4:
  try:
    # Menu
    print('============================================')
    print('  Digite [1] se você for do sexo masculino  ')
    print('  Digite [2] se você for do sexo feminino  ')
    print('============================================')
    # Entrada de dados
    sexo = int(input(''))
    # Tratamento de erro
    if sexo > 2 or sexo < 1:
      print('ERRO: apenas digite [1] ou [2] para informar o seu sexo!')
    else:
      if sexo == 1: # Contagem do sexo masculino
        # Entrada de dados
        altura_masculina = float(input('Informe sua altura em metros (Mínimo de 0.40 metros e máxima de 3 metros): '))
        # Tratamento de erro
        if altura_masculina < 0.40 or altura_masculina > 3.00:
          print('ERRO: a altura mínima é de 0.40 metros (40 centímetros) e máxima de 3 metros!')
        else: # Soma das alturas dos homens
          contador += 1
          sexo_masculino += 1
          altura_media_masculina += altura_masculina
      else: # Contagem do sexo feminino
        # Entrada de dados
        altura_feminina = float(input('Informe sua altura em metros (Mínimo de 0.40 metros e máxima de 3 metros): '))
        # Tratamento de erro
        if altura_feminina < 0.40 or altura_feminina > 3.00: 
          print('ERRO: a altura mínima é de 0.40 metros (40 centímetros) e máxima de 3 metros!')
        else: # Soma das alturas das mulheres
          contador += 1
          sexo_feminino += 1
          altura_media_feminina += altura_feminina
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
# Resultado
if sexo_feminino > 0:
  altura_media_feminina /= sexo_feminino
  print(f'A média de altura entre as mulheres é {altura_media_feminina:.2f} metros')
if sexo_masculino > 0:
  altura_media_masculina /= sexo_masculino
  print(f'A média de altura entre os homens é {altura_media_masculina:.2f} metros')
