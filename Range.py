# usando Range gerando uma sequencia de numeros:
"""
for contador in range(1, 11, 1):
    print(contador)
"""
#outra forma de uso
"""
for contador in range(11):
    print(contador)
"""
#Pode ser usado em conjunto com o list
"""
numeros = list(range(11))
print(numeros)
"""
#Pode-se ainda definir o 'step' o 'passo' ou 'incremento' do range
for contador in range(0, 11, 2):
    print(contador)