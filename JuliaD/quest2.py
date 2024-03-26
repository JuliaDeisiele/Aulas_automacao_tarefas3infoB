'''3) Crie um programa que solicita como entrada uma string representando
uma cor (verde, amarelo ou vermelho). Caso a cor seja vermelha, o
programa deve imprimir 'pare'; se for amarela, imprimir 'atenção'; e se for
verde, imprimir 'siga'.'''

cor = (input('Digite uma cor (verde, amarelo ou vermelho): '))

if cor == "vermelho":
    print ('Pare')
elif cor == "amarelo":
    print ('Atenção')
else:
    print('Siga')