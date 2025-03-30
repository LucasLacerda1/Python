# Declaração de variável
contador = 0
temperatura = 0
soma = 0
media = 0
while True: # Loop
  try:
    contador += 1
    print(f'Informe a temperatura do {contador}º dia (mínimo 28°C):')
    # Entrada de dados
    temperatura = float(input(''))
    soma += temperatura
    media = soma / contador
    if temperatura <= 28:
      # Resultado
      print('FIM DO PROGRAMA')
      print(f'A temperatura média do verão capixaba é: {media:.1f}°C!')
      break # Quebra do loop
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
