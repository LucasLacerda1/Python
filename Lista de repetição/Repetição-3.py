# Declaração de vairável
Q = 0
try:
  # Entrada de dados
  N = int(input('Informe o valor de N (N deve ser maior ou igual a 2): '))
  LI = int(input('Informe o limite inferior (Deve pertencer aos números naturais):'))
  LS = int(input('Informe o limite inferior (Deve pertencer aos números naturais):'))

  # Tratamento de erro
  if N < 2 or LI < 0 or LS < 0 or LI > LS:
    print('ERRO: Dados de entrada')
  else:
    # Verificação de N
    for contador in range (LI, LS):
      if contador % N == 0:
        Q += 1
        print(f'{Q}º número: {contador}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}') 
