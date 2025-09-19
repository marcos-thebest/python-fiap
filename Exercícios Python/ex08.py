p1 = float(input('Digite o valor do primeiro produto: '))
p2 = float(input('Digite o valor do segundo produto: '))
p3 = float(input('Digite o valor do terceiro produto: '))
p4 = float(input('Digite o valor do quarto produto: '))
p5 = float(input('Digite o valor do quinto produto: '))
p = float(input('\nDigite o valor do pagamento: '))
t = (p1+p2+p3+p4+p5)
f = p - t
print(f'O valor do troco é: R${f:.2f}')