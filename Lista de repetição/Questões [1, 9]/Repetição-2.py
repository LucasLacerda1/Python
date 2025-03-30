# Declaração de variável
Q = 0
M = 0
S = 0
try:
  for contador in range(200, 99, -1):
    if contador % 11 == 0:
      Q += 1
      print(f'{Q}º número: {contador}')
      S += contador
  M = S / Q
  print(f'A soma dos números múltiplos de 11 de 200 a 100 é: {S}')
  print(f'A média dos números múltiplos de 11 de 200 a 100 é: {M:.0f}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}') 
