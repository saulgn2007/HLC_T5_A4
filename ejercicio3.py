def potencia(base, exponente):
    cont=1
    for i in range(1,exponente+1):
        cont= cont*base 
    return cont

print(potencia(2, 9))