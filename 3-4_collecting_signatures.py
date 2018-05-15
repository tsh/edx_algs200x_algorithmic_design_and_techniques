def dataset():
    with open('data/3_4_covering_segments.in') as f:
        n = int(f.readline().strip())
        points = []
        for _ in range(n):
            points.append(tuple(map(int, f.readline().split())))
    return points


def calculate(segments):
    points = []
    segments.sort(key=lambda x: x[1])
    while segments:
        min_right = segments[0][1]
        points.append(min_right)
        i = 0
        while i < len(segments):
            if segments[i][0] <= min_right <= segments[i][1]:
                del segments[i]
            else:
                i += 1
    return len(points), points


if __name__ == '__main__':
    assert calculate([(1,3), (2,5), (3,6)]) == (1, [3])
    assert calculate([(1,4), (2,3), (1,3), (3,6)]) == (1, [3])
    assert calculate([(4,7), (1,3), (2,5), (5,6)]) == (2, [3, 6])
    print(calculate(dataset()))