def dataset():
    with open('data/4_1_binary_search.in') as f:
        a = list(map(int, f.readline().split()))[1:]
        b = list(map(int, f.readline().split()))[1:]
    return a, b


def binary_search(a, low, high, key):
    if high < low:
        return -1
    mid = int((low+high)/2)
    if a[mid] == key:
        return mid
    elif a[mid] > key:
        return binary_search(a, low, mid - 1, key)
    else:
        return binary_search(a, mid + 1, high, key)

def search(a, keys):
    res = []
    for key in keys:
        res.append(binary_search(a, 0, len(a)-1, key))
    return res

if __name__ == '__main__':
    assert search([1,5,8,12,13], [8,1,23,1,11]) == [2,0,-1,0,-1]
    print(len(list(filter(lambda x: x>=0, search(*dataset())))))