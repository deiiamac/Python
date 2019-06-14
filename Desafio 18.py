from math import radians, sin, cos, tan
n = float(input('Digite o angulo: '))
seno = sin(radians(n))
cos = cos(radians(n))
tan = tan(radians(n))
print('O angulo de {} tem o SENO de {:.2f} '
      '\nO angulo de {} tem o COSSENO de {:.2f} '
      '\nO angulo de {} tem a TANGENTE de {:.2f}'.format(n, seno, n, cos, n, tan))