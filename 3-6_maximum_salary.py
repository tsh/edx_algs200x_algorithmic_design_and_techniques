def dataset():
    with open('data/3_6_largest_number.in') as f:
        _ = f.readline()
        items = list(map(int, f.readline().split()))
    return items


def is_greater_or_equal(a, b):
    if b is None:
        return True
    a, b = str(a), str(b)
    if int(a+b) > int(b+a):
        return True
    else:
        return False


def largest_number(items):
    result = ''
    while items:
        max_digit = None
        for item in items:
            if is_greater_or_equal(item, max_digit):
                max_digit = item
        result+=str(max_digit)
        items.remove(max_digit)
    return int(result)


if __name__ == '__main__':
    assert largest_number([21, 2]) == 221
    assert largest_number([9,4,6,1,9]) == 99641
    assert largest_number([23, 39, 92]) == 923923
    print(largest_number(dataset()))