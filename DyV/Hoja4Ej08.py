
def potenciasDyV(x,a):
    if a == 0:
        result = 1
    else:
        if a == 1:
            result = x
        else:
            if a % 2 == 0:
                aux = potenciasDyV(x, a // 2)
                result = aux * aux
            else:
                result = x * potenciasDyV(x,a-1)
    return result

print('Cálculo de x**a con un enfoque de Divide y Vencerás')
x = float(input('Valor de x?: '))
a = int(input('Valor de a?: '))
print('x**a=',potenciasDyV(x,a))