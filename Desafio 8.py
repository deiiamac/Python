#Desafio 8

medida = float(input('Digite a medida em metros: '))
km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print('A medida de {} corresponde a: \n{}km \n{}hm \n{}dam \n{}dm \n{}cm \n{}mm' .format(medida, km, hm, dam, dm, cm, mm))

#n = float(input('Digite a distancia: '))
#print ('a medida de {} m corresponde a \n{:.0f} cm \n{:.0f} mm' .format(n, n*100, n*1000))