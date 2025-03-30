# Declaração de variável
contador = 0 # Enumerar
diabete = 0
idade = 0
massa = 0.0
taxa = 0.0
while contador < 50: # loop
  try:
    # Entrada de dados
    idade = int(input('Informe sua idade: '))
    massa = float(input('Informe seu peso: '))
    diabete = int(input('Digite [0] se não for diabético, digite [1] se for diabético: '))
    # Tratamento de erro
    if idade <= 0 or massa <= 0 or diabete > 1 or diabete < 0:
      print('ERRO: dados de entrada!')
    else:
      contador += 1
      if diabete == 0:
        taxa = (0.98 * massa ** 0.5) / (1.08 * massa)
        # Resultado
        print(f'O {contador}º paciente, sendo não diabético tem a taxa média de glicose de: {taxa:.2f}')
      else:
        taxa = massa ** 0.5 / (0.93 * massa)
        # Resultado
        print(f'O {contador}º paciente, sendo diabético tem a taxa média de glicose de: {taxa:.2f}')
  except Exception as ERRO_EXCECAO:
    print(f'ERRO: {ERRO_EXCECAO}')
