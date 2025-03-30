# Declaração de variável
candidato_1 = 0
candidato_2 = 0
contador = 0
nulo = 0
porcentagem_candidato_1 = 0.0
porcentagem_candidato_2 = 0.0
porcentagem_nulo = 0.0
voto = 0
# Menu
print('   Eleção para síndico do condomínio!'   )
print('========================================')
print('  Digite [1] para votar no candidato 1  ')
print('  Digite [2] para votar no candidato 2  ')
print('  Digite [0] para votar nulo  ')
print('========================================')
try:
  while contador < 10:
    contador += 1
    # Entrada de dados
    voto = int(input(''))
    if voto > 2:
      print('ERRO: Digite [1] ou [2] ou [0] para votar!')
    elif voto == 1:
      candidato_1 += 1
    elif voto == 2:
      candidato_2 += 1
    else:
      nulo += 1
  if candidato_1 > 0:
    porcentagem_candidato_1 = (candidato_1 / contador) * 100
    print(f'{porcentagem_candidato_1}% votaram no candidato 1!')
  if candidato_2 > 0:
    porcentagem_candidato_2 = (candidato_2 / contador) * 100
    print(f'{porcentagem_candidato_2}% votaram no candidato 2!')
  if nulo > 0:
    porcentagem_nulo = (nulo / contador) * 100
    print(f'{porcentagem_nulo}% votaram nulo!')
  if porcentagem_candidato_1 > porcentagem_candidato_2:
    print('O candidato 1 ganhou a eleição, parabéns!')
  elif porcentagem_candidato_2 > porcentagem_candidato_1:
    print('O candidato 2 ganhou a eleição, parabéns!')
except Exception as ERRO_EXCECAO:
  print(f'ERRO DE EXCEÇÃO: {ERRO_EXCECAO}')
