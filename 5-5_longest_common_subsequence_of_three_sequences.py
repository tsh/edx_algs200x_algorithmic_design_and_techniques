def dataset():
    with open('data/5_5_lcs3.in') as f:
        f.readline()
        str1 = f.readline().strip().split()
        f.readline()
        str2 = f.readline().strip().split()
        f.readline()
        str3 = f.readline().strip().split()
    return str1, str2, str3


def lcs(str1, str2, str3):
    table = [[[None]*(len(str3)+1) for _ in range(len(str2)+1)] for _ in range(len(str1)+1)]
    for i in range(len(str1) + 1):
        for j in range(len(str2) + 1):
            for k in range(len(str3) + 1):
                if i == 0:
                    table[i][j][k] = 0
                elif j == 0:
                    table[i][j][k] = 0
                elif k == 0:
                    table[i][j][k] = 0
                elif str1[i-1] == str2[j-1] == str3[k-1]:
                    table[i][j][k] = table[i-1][j-1][k-1] + 1
                else:
                    table[i][j][k] = max(table[i-1][j][k], table[i][j-1][k], table[i][j][k-1])
    return table[i][j][k]

if __name__ == '__main__':
    print(lcs(['1', '2', '3'], ['2','1','3'], ['1', '3', '5']))  # 2
    print(lcs(['8', '3', '2', '1', '7'], ['8', '2', '1', '3', '8', '10', '7'], ['6', '8', '3', '1', '4', '7']))  # 3
    print(lcs(*dataset()))