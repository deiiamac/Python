#Desafio 11

#largura=float(input('Largura da parede: '))
#altura=float(input('Altura da parede: '))
#area=largura*altura
#tinta=area/2
#print('Sua parede tem a dimensão de {}x{} e sua aréa é de {}m²' .format(largura, altura, area))
#print('Para pintar essa parede, voce precisara de {}l de tinta.' .format(tinta))

lar = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
print ('A parede tem dimensão de {}x{} e sua área é {}m²'.format(lar,alt,(lar*alt)))
print ('para pintar essa parede, vc precisa de {}L de tinta' .format((lar*alt) / 2))