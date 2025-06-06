import numpy as np

''' Letra A)
Exibir na Tela (Precisão de uma (1) casa decimal: .1f): Média Individual, 1° Bimestre, 2° Bimestre, Semestral e Final (após a Prova Final).

Nota da Prova Final é lida (INPUT) do usuário, somente para os que estão de Prova Final.'''

# Preenchimento automático da Prova Final
media = (dataset4[:,1] + dataset4[:,2]) / 2
media[:5]

ProvaFinal = np.zeros(len(dataset4))
mean = 5.0
std = 0.9
ProvaFinal[indexProvaFinal] = np.random.normal(mean, std, sum(indexProvaFinal))
''' Letra B)
A quantidade: Absoluta e Relativa dos alunos com STATUS: Aprovados (sem Prova Final), Prova Final, Aprovados (com Prova Final) e Reprovados.'''

notas1 = dataset4[:, 1]
notas2 = dataset4[:, 2]
media_sem_pf = (notas1 + notas2) / 2

nota_pf = np.zeros(len(dataset4))

index_pf = (media_sem_pf >= 4) & (media_sem_pf < 7)

nota_pf[index_pf] = np.random.normal(5, 0.9, np.sum(index_pf))

media_final = media_sem_pf
media_final[index_pf] = (media_sem_pf[index_pf] + nota_pf[index_pf]) / 2

aprovados_sem_pf = media_sem_pf >= 7
aprovados_com_pf = index_pf & (media_final >= 5)
reprovados = (media_sem_pf < 4) | (index_pf & (media_final < 5))

qtd_aprov_sem_pf = np.sum(aprovados_sem_pf)
qtd_aprov_com_pf = np.sum(aprovados_com_pf)
qtd_reprovados   = np.sum(reprovados)
qtd_pf           = np.sum(index_pf)

total_alunos = len(dataset4)

rel_aprov_sem_pf = qtd_aprov_sem_pf / total_alunos * 100
rel_aprov_com_pf = qtd_aprov_com_pf / total_alunos * 100
rel_reprovados   = qtd_reprovados / total_alunos * 100
rel_pf           = qtd_pf / total_alunos * 100

print(f'Total de alunos: {total_alunos}\n')

print(f'Aprovados sem Prova Final: {qtd_aprov_sem_pf} alunos ({rel_aprov_sem_pf:.2f}%)')
print(f'Alunos que fizeram Prova Final: {qtd_pf} alunos ({rel_pf:.2f}%)')
print(f'Aprovados com Prova Final: {qtd_aprov_com_pf} alunos ({rel_aprov_com_pf:.2f}%)')
print(f'Reprovados: {qtd_reprovados} alunos ({rel_reprovados:.2f}%)')
''' Letra C)
Quantidade: Absoluta e Relativa de alunos com Média Semestral maior ou igual a um valor de média lido do usuário.'''

limite = float(input("Digite o valor mínimo da média: "))

filtro = media_sem_pf >= limite

quantidade_absoluta = np.sum(filtro)

quantidade_relativa = (quantidade_absoluta / len(media_sem_pf)) * 100

print(f"\nQuantidade absoluta de alunos com média >= {limite:.1f}: {quantidade_absoluta}")
print(f"Quantidade relativa: {quantidade_relativa:.1f}%")
''' Letra D)
Exibir na Tela (Precisão de uma (1) casa decimal: .1f):

os 10 maiores Coeficiente de Rendimento ( CR ) da turma, conforme fórmula a seguir:'''

# CRIAR CR
nota1 = dataset4[:, 1]
nota2 = dataset4[:, 2]
cr = (40 * nota1 + 60 * nota2) / 100

# APLICAR ARGSORT (ordem crescente de índice)
indices_cr_ordenado = np.argsort(cr)

# OR + ENUMERATE: FATIAMENTO DOS 10 ÚLTIMOS (ou seja, os 10 maiores CRs)
print('TOP 10 COEFICIENTES DE RENDIMENTO:\n')
for posicao, indice in enumerate(indices_cr_ordenado[-10:]):
    print(f'{posicao + 1}º lugar - Matrícula: {int(dataset4[indice, 0])}, CR: {cr[indice]:.1f}')
''' Letra E)
Pesquisar e exibir todos os dados de um aluno por sua matrícula:'''

matricula = int(input("Digite a matrícula do aluno: "))

indice = np.where(dataset4[:, 0] == matricula)[0]

if indice.size > 0:
    aluno = dataset4[indice[0]]
    print('\nDADOS DO ALUNO ENCONTRADO:')
    print(f'Matrícula          : {int(aluno[0])}')
    print(f'Nota do 1º Bimestre: {aluno[1]:.1f}')
    print(f'Nota do 2º Bimestre: {aluno[2]:.1f}')
else:
    print("Matrícula não encontrada.")
