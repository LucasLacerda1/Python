# Declaração de variável
contador = 0
soma = 0
while True: # Loop
  try:
    print(f'Informe a temperatura do {contador + 1}º dia (mínimo de -15°C e máximo de 5°C):')
    # Entrada de dados
    temperatura = float(input(''))
    # Condição para realizar o soma
    if temperatura >= -15 and temperatura <= 5:
      contador += 1
      soma += temperatura # Soma da temperatura dos dias
    else:
      if contador == 0:
        print('Não houve dias registrados no inverno!')
      else:
        media = soma / contador # Média na temperatura da estação
        # Resultado
        print(f'A temperatura média do inverno foi de: {media:.1f}°C!')
      print('FIM DO PROGRAMA!')
      break # Quebra do loop
  except Exception as ERRO_EXCECAO:
    print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
