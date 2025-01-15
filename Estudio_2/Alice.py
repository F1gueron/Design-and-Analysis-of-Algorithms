movimientos = [(0,1),(1,0),(-1,0),(0,-1)]
movimientosExtra = [(0,1),(1,0),(-1,0),(0,-1),(1,1),(-1,1),(1,-1),(-1,-1)]


def isFeasible(newX, newY, matrix,visited):
    return 0 <= newX < len(matrix) and 0<=newY<len(matrix[0]) and matrix[newX][newY] != 't' and (newX,newY) not in visited


def solve(matrix, start, end, recompensa, pos=None, index=0, cogidas = 0, visited=None,mejorSol=float('inf')):
    if visited is None:
        visited = set()
    if pos == None:
        pos = start
        visited.add(pos)
    actX,actY = pos
    if recompensa == cogidas and pos == end:
        return index
        #return min(result,mejorSol)
    else:
        for dx,dy in movimientos:
            newX,newY = actX+dx,actY+dy
            if isFeasible(newX,newY,matrix,visited):
                visited.add((newX,newY))
                if matrix[newX][newY] == 'r':
                    cogidas +=1
                result = solve(matrix, start, end, recompensa, (newX,newY), index+1, cogidas, visited,mejorSol)
                if result is not None:
                    mejorSol = min(result,mejorSol)
                if matrix[newX][newY] == 'r':
                    cogidas -= 1
                visited.remove((newX, newY))
    return mejorSol




n,m = map(int,input().strip().split())
matrix = []

for i in range(n):
    lista = list(input().strip().split())
    matrix[i].append(lista)
recompensa = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] == 'e':
            end = (i,j)
        if matrix[i][j] == 's':
            start = (i,j)
        if matrix[i][j] == 'r':
            torreta = False
            for dx,dy in movimientosExtra:
                if matrix[i+dx][j+dy] == 't':
                    torreta = True
            if not torreta:
                recompensa+=1

solve(matrix,start,end,recompensa)