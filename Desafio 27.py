nome = str(input('Digite seu nome completo: ')) .strip()
n2 = nome.split()
print('Muito Prazer em te conhecer!!')
print('Seu primeiro nome é {}' .format(n2[0]))
print('Seu ultimo nome é {}' .format(n2[len(n2)-1]))
