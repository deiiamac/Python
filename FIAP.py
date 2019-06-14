#Desafio 12

valor = float(input('Valor do produto: R$'))
desconto=float(input('Desconto em %'))
novo = valor - (valor*desconto/100)
faltar = novo - 750
print('O Faculade que custava {}, com a bolsa de {}% vai custar {:.2f}'. format(valor, desconto, novo))
print('Vai faltar {}'.format(faltar))