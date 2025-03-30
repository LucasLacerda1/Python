import math
try:
  # Entrada de dados
  R = float(input('Qual o raio da esfera? '))
  # Tratamento de erro
  if(R <= 0):
    print('O Raio deve ser maior que 0!!')
  else:
    # Cálculo da área e volume
    A = 4 * math.pi * (R ** 2)
    V = 4/3 * math.pi * (R ** 3)
  print(f'A área da esfera é: {A:.2f} m²')
  print(f'O volume da esfera é: {V:.2f} m³')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
