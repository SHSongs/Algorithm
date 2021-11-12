from copy import deepcopy


def solution(matrix, r):
    if r % 4 == 0:
        return matrix

    n = len(matrix)
    answer = [[0] * n for _ in range(n)]

    for _ in range(r):

        for i in range(n):
            for j in range(n):
                answer[j][n - i - 1] = matrix[i][j]
        matrix = deepcopy(answer)


    return answer


solution([[1, 2], [3, 4]], 1)
solution([[1, 2], [3, 4]], 2)
solution([[1, 2], [3, 4]], 3)
solution([[1, 2], [3, 4]], 4)
