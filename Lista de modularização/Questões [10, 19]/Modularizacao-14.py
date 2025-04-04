# CRIAR A FUNÇÃO AQUI:
valor = 7.00
def estacionamento(HH, SH, MM, SM):
  entrada_total = HH * 60 + MM
  saida_total = SH * 60 + SM
  if saida_total < entrada_total:
    saida_total += 24 * 60
  tempo_total = saida_total - entrada_total
  hora_total = tempo_total // 60
  if tempo_total <= 60:
    taxa = 0.00
  else:
    taxa = valor * hora_total
  return taxa


# MENU: REUSABILIDADE
try:
  # Entrada de dados
  print('Informe o horário de entrada')
  ENTRADA = input('HH:MM: ')
  HHMM = ENTRADA.split(':')
  HH = int(HHMM[0])
  MM = int(HHMM[1])
  print('Informe o horário de saída')
  SAIDA = input('HH:MM: ')
  SHM = SAIDA.split(':')
  SH = int(SHM[0])
  SM = int(SHM[1])
  # Tratamento de erro
  if SH < 0 or HH < 0 or SH > 23 or HH > 23:
    print('ERRO: Dados de entrada!')
    print('Informe as horas apenas de 0 a 23!')
  elif SM < 0 or MM < 0 or SM > 59 or MM > 59:
    print('ERRO: Dados de entrada!')
    print('Informe os minutos apenas de 0 a 59!')
  elif SH - HH > 23 or (HH > SH and 24 - HH + SH > 23):
    print('O tempo máximo de permanência é de 24 horas!')
  else:
    valor_total = estacionamento(HH, SH, MM, SM)
    # Resultado
    print(f'Total a pagar: R${valor_total:.2f}')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
