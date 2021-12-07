def rotate(matrix):
    n = len(matrix)

    # 전치
    for i in range(n):
        for j in range(n):
            if i != j and i < j:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 행 변환
    for i in range(n):
        matrix[i].reverse()

    print(matrix)
    return matrix


def solution(matrix):
    n = len(matrix)
    answer = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            answer[j][n - i - 1] = matrix[i][j]

    print(answer)
    return answer


rotate([[1, 2], [3, 4]])
rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
