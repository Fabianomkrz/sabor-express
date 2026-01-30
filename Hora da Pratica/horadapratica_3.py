# 1 - Crie uma lista para cada informação a seguir:

# Lista de números de 1 a 10;
# Lista com quatro nomes;
# Lista com o ano que você nasceu e o ano atual.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nomes = ['Fabiano', 'Ana', 'Alcides', 'Olga']
ano = [2002, 2026]

# 2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    print(f'{numero}')

# 3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10.

# Minha Tentativa:

soma_impares = 0
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    if numero % 2 != 0:
        soma_impares += numero
print(soma_impares)

# Correção do orientador

soma_impares = 0
for i in range(1, 11, 2):
    soma_impares += i
print(soma_impares)

# 4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente.

for i in range(10, 0, -1):
    print(i)

# 5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10.

numero = int(input('Digite um número '))
for i in range(1, 11):
    resultado = numero * i
    print(resultado)

# 6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções.

soma = 0
numeros = [1,2,3,4,5,6,7,8,9,'n']
try:
    for i in numeros:
        soma += i
    print(soma)
except:
    print('Erro')

# Correção do orientador

lista_numeros = [10, 5, 8, 3, 7]
soma = 0

try:
    for numero in lista_numeros:
        soma += numero
    print(f"Soma dos elementos: {soma}")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# 7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia.

lista = [1,2,3,4,5,6,7,8,9]
soma = 0

try:
    for numero in lista:
        soma += numero
    media = soma / len(lista)
    print(f'A média dos valores é: {media}')
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")

# Correção do orientador

lista_valores = [15, 20, 25, 30]
soma_valores = 0

try:
    for valor in lista_valores:
        soma_valores += valor
    media = soma_valores / len(lista_valores)
    print(f"Média dos valores: {media}")
except ZeroDivisionError:
    print("A lista está vazia, não é possível calcular a média.")
except Exception as e:
    print(f"Ocorreu um erro: {e}")