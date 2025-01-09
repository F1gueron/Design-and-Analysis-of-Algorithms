#Mochila 0-1
import copy


def inicializarDatos():
    datos = {} #es opcional
    datos['N'] = 4
    datos['W'] = 8
    datos['Peso'] = [2,3,4,5]
    datos['Valor'] = [3,5,6,10]
    return datos

def inicializarSolucion(datos):
    sol = {}
    sol['PesoAc'] = 0
    sol['ValorAc'] = 0
    sol['Objetos'] = [0] * datos['N']
    return sol

def mejor(mejorSol, sol):
    if sol['ValorAc'] > mejorSol['ValorAc']:
        return copy.deepcopy(sol)
    return mejorSol

def esSolucion(sol, datos):
    return sol['PesoAc'] + min(datos['Peso']) > datos['W']

def esFactible(sol, datos, i):
    return sol['PesoAc'] + datos['Peso'][i] <= datos['W']

def asignar(sol, i, datos):
    sol['PesoAc'] += datos['Peso'][i]
    sol['ValorAc'] += datos['Valor'][i]
    sol['Objetos'][i] += 1
    return sol

def borrar(sol, i, datos):
    sol['PesoAc'] -= datos['Peso'][i]
    sol['ValorAc'] -= datos['Valor'][i]
    sol['Objetos'][i] -= 1
    return sol


def mochilaVA(sol, mejorSol, datos, k):
    if esSolucion(sol, datos): #caso base
        mejorSol = mejor(mejorSol, sol)
    else: #caso recursivo
        for i in range(k, datos['N']):
            if esFactible(sol, datos, i):
                sol = asignar(sol, i ,datos)
                mejorSol = mochilaVA(sol, mejorSol, datos, i)
                sol = borrar(sol, i, datos)
    return mejorSol

datos = inicializarDatos()
sol = inicializarSolucion(datos)
mejorSol = inicializarSolucion(datos)
mejorSol = mochilaVA(sol, mejorSol, datos, 0)
print(mejorSol)
