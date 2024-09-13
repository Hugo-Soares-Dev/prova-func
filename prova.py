"""Desenvolva um programa em Python que permita ao usuário digitar várias notas. Em seguida, crie uma função chamada "calcular_media" que irá receber as notas digitadas e calcular a média do aluno. Também crie uma função chamada "verificar_situacao" que, com base na média calculada, irá exibir a situação do aluno: "Reprovado" se a média for menor que 7, "Aprovado" se a média for maior ou igual a 7, e "Parabéns, sua média é 10" se a média for igual a 10."""

def calcular_media(list):
 media = sum(list)/len(list)
 return media

def verificar_situacao(media):
   if media == 10:
      return 'Parabens!!'
   elif media < 10 and media >= 7:
      return 'Aprovado!'
   else: 
      return 'Reprovado'
      
notas = []

while True:
    nota = int(input('digite sua nota, ou (00) para sair: '))
    if nota == 00:
        break
    else:
        notas.append(nota)

media = calcular_media(notas)
verificar = verificar_situacao(media)

print(f'A media do aluno foi de: {media:.2f} Pts.\n{verificar}')