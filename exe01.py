nota = list()

def media_das_notas(notas):
    media = sum(notas) / len(notas)
    return media

while True:
    nota_aluno = float(input("Nota do aluno: "))
    nota.append(nota_aluno)

    opn = input("Deseja continuar? [Y/N]: ").upper()

    if opn == 'N':
        break

media = media_das_notas(nota)


print(f'Notas inseridas: {nota}')
print(f"MEDIA DAS NOTAS: {media}") 

if media >= 7:
    print('O aluno está aprovado.')
else:
    print('O aluno reprovado.')
