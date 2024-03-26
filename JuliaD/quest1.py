'''Cássia precisa de ajuda para calcular a quantidade de gotas de
medicamento para sua filha. Construa um programa que solicite a
concentração de princípio ativo do medicamento em mg/ml, o peso da
criança e a dose recomendada em mg por kg. O programa deve calcular a
dose total multiplicando o peso da criança pela dose por kg recomendada
e dividindo pelo conteúdo do medicamento em mg por ml. Para obter a
quantidade de gotas, multiplica-se o resultado por 20, já que 1 ml equivale
a aproximadamente 20 gotas.'''

concentracao = float (input('Digite a concentração do princípio ativo do medicamento em mg/ml: '))
peso = float (input('Digite o peso da criança: '))
dose = float (input('Digite a dose recomendada em mg por kg: '))

doseTotal = (peso * dose) / concentracao
gotas = (doseTotal * 20)

print ('\nDose total igual a', doseTotal,'mg por kg')
print ('O total de gotas a serem tomadas é', gotas,'gotas')
