
def medianaDyV(v1,iniV1,finV1,v2,iniV2,finV2):
    if iniV1 == finV1 and iniV2 == finV2:  # Vectores de longitud 1
        return min(v1[iniV1], v2[iniV2])
    else:
        if iniV1 == finV1-1 and iniV2 == finV2-1: # Vectores de longitud 2, que tenemos que tratar también como caso especial
            if v1[finV1] < v2[iniV2]:
                return v1[finV1]
            else:
                if v2[finV2] < v1[iniV1]:
                    return v2[finV2]
                else:
                    return max(v1[iniV1],v2[iniV2])
        else: # Caso general
            medV1 = (iniV1 + finV1) // 2
            medV2 = (iniV2 + finV2) // 2
            if v1[medV1] == v2[medV2]:
                return v1[medV1]
            else:
                if v1[medV1] < v2[medV2]:
                    return medianaDyV(v1, medV1, finV1, v2, iniV2, medV2)
                else:
                    return medianaDyV(v1, iniV1, medV1, v2, medV2,finV2)


v1 = [1,2,3,4,6,7,8,10]
v2 = [0,5,9,11,12,13,14,15]
print(v1)
print(v2)
print('la mediana es:',medianaDyV(v1,0,len(v1)-1,v2,0,len(v2)-1))