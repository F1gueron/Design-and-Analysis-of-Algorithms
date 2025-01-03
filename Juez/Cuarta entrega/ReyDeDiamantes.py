def rec_bs(v, number, low, high):
    if low > high:  # caso base
        return -low - 1

    mid = (low + high) // 2
    if v[mid] == number:
        return mid
    elif number < v[mid]:
        return rec_bs(v, number, low, mid - 1)
    else:
        return rec_bs(v, number, mid + 1, high)


def recBinarySearch(v, number):
    return rec_bs(v, number, 0, len(v) - 1)


def kill_players(matrix, attacked, n):
    twoDimensionMatrix = [matrix[i][j] for i in range(n) for j in range(n)]  # 3D to 2D
    eliminated_positions = set()

    for numero in attacked:
        index = recBinarySearch(twoDimensionMatrix, numero)
        if index >= 0:
            while index < len(twoDimensionMatrix) and (index in eliminated_positions or twoDimensionMatrix[index] == "X"):
                index += 1
        else:
            index = -index - 1
            while index < len(twoDimensionMatrix) and (index in eliminated_positions or twoDimensionMatrix[index] == "X"):
                index += 1

        if index < len(twoDimensionMatrix):
            eliminated_positions.add(index)

    result = []
    for i in range(n):
        row_start = i * n
        row_end = (i + 1) * n
        row = twoDimensionMatrix[row_start:row_end]

        for j in range(len(row)):
            idx = row_start + j
            if idx in eliminated_positions:
                row[j] = 'X'
        result.append(row)
    return result


if __name__ == "__main__":
    n = int(input())
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    attacked = list(map(int, input().split()))
    result = kill_players(matrix, attacked, n)
    for fila in result:
        print(' '.join(map(str, fila)))
