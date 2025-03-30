# Import de biblioteca
import numpy as np
# Declaração de variável
contador = 0
menor_tempo = np.inf
vencedor = 0

while contador < 20000: # Loop
  try:
    # Entrada de dados
    inscricao = int(input('Insira o seu número de inscrição: '))
    # Tratamento de erro
    if inscricao <= 0:
      print('O número de inscrição deve ser maior que 0!')
    else:
      # Entrada de dados
      tempo_prova = float(input('Insira o tempo de prova (em minutos): '))
      # Tratamento de erro
      if tempo_prova <= 0:
        print('ERRO: dados de entrada')
      else:
        contador += 1
        if tempo_prova < menor_tempo:
          menor_tempo = tempo_prova
          vencedor = inscricao
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
# Resultado
print(f'O maratonista {vencedor} é o vencedor da prova com {menor_tempo} minutos! ')
