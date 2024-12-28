from collections import deque

# Movimientos posibles en la matriz
moves = [[1, 0], [-1, 0], [0, 1], [0, -1]]


def notTurret(newX, newY, n, m, matriz):
    """Verifica si la posición (newX, newY) no está cerca de una torreta ('t')."""
    for cX, cY in moves:
        postX, postY = newX + cX, newY + cY
        if 0 <= postX < n and 0 <= postY < m and matriz[postX][postY] == 't':
            return False
    return True


def bfs(matriz, n, m, start, recompensas, win):
    """Búsqueda por amplitud para encontrar el camino más corto recolectando todas las recompensas."""
    q = deque([(start[0], start[1], 0, frozenset())])  # (x, y, pasos, recompensas_recolectadas)
    visited = {(start[0], start[1], frozenset())}  # (x, y, recompensas_recolectadas)

    while q:
        x, y, pasos, puntos = q.popleft()

        # Verificar si hemos llegado a la meta con todas las recompensas
        if len(puntos) == recompensas and (x, y) == win:
            return pasos +1

        # Explorar vecinos
        for cX, cY in moves:
            newX, newY = x + cX, y + cY

            # Validar movimiento
            if (
                0 <= newX < n
                and 0 <= newY < m
                and matriz[newX][newY] != 'w'
                and notTurret(newX, newY, n, m, matriz)
            ):
                # Actualizar recompensas recolectadas
                nuevos_puntos = puntos | {(newX, newY)} if matriz[newX][newY] == 'r' else puntos
                estado = (newX, newY, frozenset(nuevos_puntos))

                if estado not in visited:
                    visited.add(estado)
                    q.append((newX, newY, pasos + 1, nuevos_puntos))

    # Si no se encuentra un camino válido
    return -1


if __name__ == "__main__":
    # Lectura de la matriz
    n, m = map(int, input().strip().split())
    matriz = []
    recompensas = 0
    start, win = None, None

    for i in range(n):
        fila = input().strip().split()
        matriz.append(fila)
        for j, c in enumerate(fila):
            if c == 's':
                start = (i, j)
            elif c == 'r':
                recompensas += 1
            elif c == 'e':
                win = (i, j)

    # Ejecutar BFS y mostrar el resultado
    print(bfs(matriz, n, m, start, recompensas, win))
