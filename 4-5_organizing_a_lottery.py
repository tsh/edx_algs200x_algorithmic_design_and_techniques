def dataset():
    with open('data/4_5_lottery.in') as f:
        n_segments, n_points = map(int, f.readline().split())
        segments, points = [], []
        for _ in range(n_segments):
            segments.append(tuple(map(int, f.readline().split())))
        points.append(list(map(int, f.readline().split())))
    return segments, points


def lottery(segments, points):
    pass


if __name__ == '__main__':
    print(lottery([(0,5), (7,10)], [1,6,11]))  # 1 0 0
    print(lottery([(-10, 10)], [-100, 100, 0]))  # 0 0 1
    print(lottery([(0,5), (-3,2), (7,10)], [1,6]))  # 2 0
    # print(lottery(*dataset()))