# Declaração de variável
Q = 0
try:
  for contador in range(3, 101, 3):
    Q += 1
    print(f'{Q}º número: {contador}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}') 
