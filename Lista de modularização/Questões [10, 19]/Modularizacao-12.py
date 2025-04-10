# CRIAR A FUNÇÃO AQUI:
def relogio(s):
  h = s // 3600
  m = (s % 3600) // 60
  s = s % 60
  return s, m, h

# Declaração de variável:
contador = 0 # Enumerar
# MENU: REUSABILIDADE
while contador < 5:
  try:
    print('\nEste programa converte os segundos que o usuário informar em hora(s) minuto(s) segundo(s).')
    s = int(input('Informe o tempo em segundo: '))
    if s < 0:
      print('ERRO: entrada de dados')
    else:
      contador += 1
      segundo, minuto, hora = relogio(s)
      print(f'Tempo: {s} segundo = {hora} hora(s) + {minuto} minuto(s) {segundo} segundo(s).')
  except Exception as erro:
    print(f'ERRO: {erro}')
