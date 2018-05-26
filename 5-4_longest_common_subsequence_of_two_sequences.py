def dataset():
    with open('data/5_4_lcs2.in') as f:
        f.readline()
        str1 = f.readline().strip().split()
        f.readline()
        str2 = f.readline().strip().split()
    return ''.join(str1), ''.join(str2)


def lcs(str1, str2):
    table = [[None]*(len(str2)+1) for _ in range(len(str1)+1)]
    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):
            if i == 0:
                table[i][j] = 0
            elif j == 0:
                table[i][j] = 0
            elif str1[i-1] == str2[j-1]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i-1][j], table[i][j-1])
    return table[i][j]

if __name__ == '__main__':
    print(lcs('275', '25'))  # 2
    print(lcs('7', '1234'))  # 0
    print(lcs('2783', '5287'))  # 2
    print(lcs(*dataset()))