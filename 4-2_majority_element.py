def dataset():
    with open('data/4_2_majority_element.in') as f:
        f.readline()
        arr = map(int, f.readline().split())
    return list(arr)


def majority(arr, return_major=False):
    if len(arr) <= 1:
        return 0
    elif len(arr) == 2 and arr[0] == arr[1]:
        return arr[0] if return_major else 1
    mid = int(len(arr) / 2)
    return majority(arr[:mid], return_major) or majority(arr[mid:], return_major)


if __name__ == '__main__':
    assert majority([2,3,9,2,2]) == 1
    assert majority([1,2,3,4]) == 0
    print(majority(dataset(), return_major=True))