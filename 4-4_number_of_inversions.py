def dataset():
    with open('data/4_4_inversions.in') as f:
        f.readline()
        data = map(int, f.readline().split())
    return list(data)


def inversions(items):
    return items


if __name__ == '__main__':
    assert inversions([2,3,9,2,9]) == 2
    # print(inversions(dataset()))