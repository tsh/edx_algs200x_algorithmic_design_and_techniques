def dataset():
    with open('data/3_4_covering_segments.in') as f:
        n = int(f.readline().strip())
        points = []
        for _ in range(n):
            points.append(tuple(map(int, f.readline().split())))
    return points

def include_point(segment, point):
    #to check segment has segment.start <= point <= segment.end
    return segment[0] <= point <= segment[1]

def choose_min_right_segment(segments):
    #choose the minmum right value in segments. Just loop through segments and choose min_right
    segments.sort(key=lambda x: x[1])
    return segments[0][1]


def calculate(segments):
    points = []

    while(len(segments) > 0):
        min_right = choose_min_right_segment(segments)
        points.append(min_right)
        i = 0
        while i < len(segments):
            if include_point(segments[i], min_right):
                del segments[i]
            else:
                i = i + 1
    return len(points), points


if __name__ == '__main__':
    assert calculate([(1,3), (2,5), (3,6)]) == (1, [3])
    assert calculate([(1,4), (2,3), (1,3), (3,6)]) == (1, [3])
    assert calculate([(4,7), (1,3), (2,5), (5,6)]) == (2, [3, 6])
    print(calculate(dataset()))