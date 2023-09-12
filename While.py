#LOOP while básico
"""
contador = 1 
#while contador <= 10:
#    print(contador)
#    contador = contador +1
"""
#LOOP while com uso da função break
"""
contador = 1 
while contador <= 10:
    print(contador)
    contador = contador +1
    if contador == 5:
        break
"""
#LOOP whie usando a função continue
"""
contador = 1 
while contador <= 10:
    contador = contador +1
    if contador == 5:
        continue
    print(contador)
"""
#LOOP while usando a função else
"""
contador = 1 
while contador < 10:
    print(contador)
    contador = contador +1
else:
    print("Não é mais menor que 10")
"""