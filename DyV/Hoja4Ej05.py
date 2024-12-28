def busquedaIndice(v,ini,fin):
    if fin < ini:
        return False
    else:
        mitad = (ini + fin) // 2
        if v[mitad] == mitad:
            return True
        else:
            if v[mitad] > mitad:
                return busquedaIndice(v,ini,mitad-1)
            else:
                return busquedaIndice(v,mitad+1,fin)

# Prog Ppal:
v = [-2,-1,0,2,3,6,7,8]
print(busquedaIndice(v,0,len(v)-1))