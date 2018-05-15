def dataset():
    with open('data/3_4_covering_segments.in') as f:
        n = int(f.readline().strip())
        points = []
        for _ in range(n):
            points.append(tuple(map(int, f.readline().split())))
    return points


def calculate(points):
    points.sort(key=lambda x: x[0])
    n = len(points)
    left = 0
    res = []
    while left <= n - 1:
        left_min, left_max = points[left]
        candidate = left_min
        for right in range(left, n):
            right_min, right_max = points[right]
            if right_min <= left_max:
                left += 1
                candidate = right_min
                continue
            else:
                left = right
                break
        res.append(candidate)
    print(res)
    return len(res), res


if __name__ == '__main__':
    # assert calculate([(1,3), (2,5), (3,6)]) == (1, [3])
    # assert calculate([(1,4), (2,3), (1,3), (3,6)]) == (1, [3])
    assert calculate([(4,7), (1,3), (2,5), (5,6)]) == (2, [3, 6])
    # print(calculate(dataset()))