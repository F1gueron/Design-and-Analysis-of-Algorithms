import copy

def inicializarSolucion(datos):
    sol = {}
    sol['PesoAc'] = 0
    sol['ValorAc'] = 0
    sol['Nombres'] = []
    sol['Objetos'] = [0] * datos['N']
    return sol

def mejor(mejorSol, sol):
    if sol['ValorAc'] > mejorSol['ValorAc'] and sol['PesoAc'] > mejorSol['PesoAc']:
        return copy.deepcopy(sol)
    return mejorSol

def esSolucion(sol, datos):
    return sol['PesoAc'] + min(datos['Peso']) > datos['W']

def esFactible(sol, datos, i):
    return sol['PesoAc'] + datos['Peso'][i] <= datos['W']

def asignar(sol, i, datos):
    sol['PesoAc'] += datos['Peso'][i]
    3603
    sol['ValorAc'] += datos['Valor'][i]
    sol['Objetos'][i] += 1
    sol['Nombres'].append(datos['Nombre'][i])
    return sol

def borrar(sol, i, datos):
    sol['PesoAc'] -= datos['Peso'][i]
    sol['ValorAc'] -= datos['Valor'][i]
    sol['Objetos'][i] -= 1
    sol['Nombres'].remove(datos['Nombre'][i])
    return sol
def mochilaVA(sol, mejorSol, datos, k):
    if esSolucion(sol, datos): #caso base
        mejorSol = mejor(mejorSol, sol)
    else: #caso recursivo
        for i in range(k, datos['N']):
            if esFactible(sol, datos, i):
                sol = asignar(sol, i, datos)
                mejorSol = mochilaVA(sol, mejorSol, datos, i + 1)
                sol = borrar(sol, i, datos)
    return mejorSol

entrada = input().strip().split()
num_objetos = int(entrada[0])
max_peso = int(entrada[1])
min_beneficio = int(entrada[2])

datos = {}
datos['N'] = num_objetos
datos['W'] = max_peso
datos['Nombre'] = []
datos['Peso'] = []
datos['Valor'] = []

for i in range(num_objetos):
    objeto = input().strip().split()
    nombre = objeto[0]
    datos['Nombre'].append(nombre)
    peso = int(objeto[1])
    datos['Peso'].append(peso)
    beneficio = int(objeto[2])
    datos['Valor'].append(beneficio)


sol = inicializarSolucion(datos)
mejorSol = inicializarSolucion(datos)

mejorSol = mochilaVA(sol, mejorSol, datos, 0)

mejorSol['Nombres'].sort()
print(*mejorSol['Nombres'])
print(f"{mejorSol['PesoAc']} {mejorSol['ValorAc']}")

if mejorSol['ValorAc'] <= min_beneficio:
    print("VUELVE")
else:
    print("SE VA")



