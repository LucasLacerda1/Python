# Declaração de variável
par = 0
impar = 0
try:
  # Percorre os números entre [10,99]
  for contador in range (10, 100):
    if contador % 2 == 0:
      par += contador
    else:
      impar += contador
  print(f'A soma dos números pares compreendidos entre [10 99]: {par}')
  print(f'A soma dos números ímpares compreendidos entre [10 99]: {impar}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
