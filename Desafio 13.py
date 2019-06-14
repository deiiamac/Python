#Desafio 13

salario = float(input('Qual é o salario do funcionario? R$'))
#novo = salario + (salario*0.15)
aumento=float(input('Quanto sera o aumento? Em porcentagem %'))
novo = salario + (salario*aumento/100)

print('Um funcionario que ganhava {}, com {} de aumento, passa a receber {}' .format(salario, aumento, novo))