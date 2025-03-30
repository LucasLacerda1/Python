# Import de biblioteca
import math
# Declaração de variável
mult = 1
numero = 0
soma = math.pi

try:
  # Entrada de dados
  numero = int(input('Informe um número inteiro e positivo maior que 0: '))
  # Tratamento de erro
  if numero < 1:
    print('ERRO: o número deve ser maior que 0!')
  else:
    for par in range(2, numero + 1, 2): # Conta apenas números pares para soma
      soma += math.pi / par
    for impar in range(1, numero + 1, 2): # Conta apenas números ímpares para multiplicação
      mult *= impar / math.pi
    # Resultado
    print(f'A soma de {numero} é: {soma:.2f}')
    print(f'A multiplicação de {numero} é: {mult:.2f}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
