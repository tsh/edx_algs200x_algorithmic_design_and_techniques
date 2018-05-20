def dataset():
    with open('data/4_4_inversions.in') as f:
        f.readline()
        data = map(int, f.readline().split())
    return list(data)


def merge(left, right, invs):
    i, j = 0, 0
    res = []
    while i < len(left) or j < len(right):
        if i == len(left):
            res.extend(right[j:])
            break
        elif j == len(right):
            res.extend(left[i:])
            break
        elif left[i] <= right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
            invs += len(left) -i
    return res, invs


def partition(items, invs):
    if len(items) < 2:
        return items, invs
    mid = int(len(items) / 2)
    left, l_inv = partition(items[:mid], invs)
    right, r_inv = partition(items[mid:], invs)
    res, inv = merge(left, right, l_inv + r_inv)
    return res, inv


def inversions(items):
    return partition(items, 0)[1]


if __name__ == '__main__':
    assert inversions([2,3,9,2,9]) == 2
    print(inversions(dataset()))