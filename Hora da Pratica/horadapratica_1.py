print('Python na Escola de Programação da Alura\n')

nome = 'Fabiano'
idade = 23
print(f'Meu nome é {nome} e tenho {idade} anos')

# Outra forma
# Abordagem do .format()
# print('Meu nome é {} e tenho {} anos.'.format(nome,idade))

print('''
A
L
U
R      
A
''')

#Outra forma: print('A','L','U','R','A',sep='\n')

# Abordagem de f-string
pi = 3.14159
print(f'O valor arredondado de pi é: {pi:.2f}')

# Outras maneiras
# Abordagem de .format()
# print('O valor arredondado de pi é: {:.2f}'.format(pi))

# Utilizando a função round()
# print('O valor arredondado de pi é:', round(pi, 2))