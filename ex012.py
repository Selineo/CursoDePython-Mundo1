v1 = float(input('qual o preço o produto R$:'))
v2 = int(input('qual o valor do deconto:%'))
s1 = (v1*v2)/100
print('na compra de um produto de valor R${} com desconto de {}%\no abate do preço sera de R${:.2f}\nvalor final do '
      'produto R${}'.format(v1, v2, s1, (v1 - s1)))
