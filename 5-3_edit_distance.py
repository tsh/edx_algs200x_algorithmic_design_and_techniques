def dataset():
    with open('data/5_3_edit_distance.in') as f:
        s1 = f.readline().rstrip()
        s2 = f.readline().rstrip()
    return s1, s2


def edit_distance(str1, str2):
    matrix = [[None for _ in range(len(str1)+1)] for _ in range(len(str2)+1)]
    for i in range(len(str2)+1):
        matrix[i][0] = i
    for j in range(len(str1)+1):
        matrix[0][j] = j

    for i in range(len(str1)):
        for j in range(len(str2)):
            m, n = i+1, j+1  # coordinates in matrix
            insertion = matrix[n][m-1] + 1
            deletion = matrix[n-1][m] + 1
            match = matrix[n-1][m-1]
            mismatch = matrix[n-1][m-1] + 1
            if str1[i] == str2[j]:
                matrix[n][m] = min(insertion, deletion, match)
            else:
                matrix[n][m] = min(insertion, deletion, mismatch)
    return matrix[n][m]


def edit_distance_refactored(str1, str2):
    matrix = [[None for _ in range(len(str1) + 1)] for _ in range(len(str2) + 1)]
    for i in range(len(str2)+1):
        for j in range(len(str1)+1):
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            elif str2[i-1] == str1[j-1]:
                matrix[i][j] = matrix[i-1][j-1]
            else:
                matrix[i][j] = 1 + min(matrix[i-1][j-1],
                                       matrix[i-1][j],
                                       matrix[i][j-1])
    return matrix[i][j]



if __name__ == '__main__':
    print(edit_distance_refactored('ab', 'ab'))  # 0
    print(edit_distance_refactored('short', 'ports'))  # 3
    print(edit_distance_refactored('editing', 'distance'))  # 5
    print(edit_distance_refactored(*dataset()))
