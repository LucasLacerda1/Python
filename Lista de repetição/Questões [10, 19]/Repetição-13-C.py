# Declaração de variável
altura_feminina = 0.00
altura_masculina = 0.00
contador = 0
homem_alto = 0
mulher_alta = 0
porcentagem_homem_alto = 0.00
porcentagem_mulher_alta = 0.00
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
          if altura_masculina > 1.82: # Verificação se o homem possui mais de 1.82 metros
            homem_alto += 1
      else: # Contagem do sexo feminino
        # Entrada de dados
        altura_feminina = float(input('Informe sua altura em metros (Mínimo de 0.40 metros e máxima de 3 metros): '))
        # Tratamento de erro
        if altura_feminina < 0.40 or altura_feminina > 3.00: 
          print('ERRO: a altura mínima é de 0.40 metros (40 centímetros) e máxima de 3 metros!')
        else: # Soma das alturas das mulheres
          contador += 1
          sexo_feminino += 1   
          if altura_feminina > 1.82: # Verificação se a mulher possui mais de 1.82 metros
            mulher_alta += 1  
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
# Verificação se há homem com mais de 1.82 metros
if homem_alto > 1:
  porcentagem_homem_alto = (homem_alto / sexo_masculino) * 100 # Cálculo da porcentagens de homens com mais de 1.82 metros
  # Resultado
  print(f'{porcentagem_homem_alto:.2f}% dos homens tem mais de 1.82 metros!')
else: # Condição de caso não tenha homem com mais de 1.82 metros
  print('Não há homens com mais de 1.82 metros registrados!')
# Verificação se há mulher com mais de 1.82 metros
if mulher_alta > 1:
  porcentagem_mulher_alta = (mulher_alta / sexo_feminino) * 100 # Cálculo da porcentagens de mulheres com mais de 1.82 metros
  # Resultado
  print(f'{porcentagem_mulher_alta:.2f}% das mulheres tem mais de 1.82 metros!')
else: # Condição de caso não tenha mulher com mais de 1.82 metros
  print('Não há mulheres com mais de 1.82 metros registrados!')
if homem_alto == 0 and mulher_alta == 0: # Condição de caso não tenha homem e mulher com mais de 1.82 metros
  print('Não há homens e mulheres com mais de 1.82 metros registrados!')
