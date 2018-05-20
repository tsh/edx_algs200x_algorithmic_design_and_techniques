def dataset():
    with open('data/4_5_lottery.in') as f:
        n_segments, n_points = map(int, f.readline().split())
        segments, points = [], []
        for _ in range(n_segments):
            segments.append(tuple(map(int, f.readline().split())))
        points.extend(list(map(int, f.readline().split())))
    return segments, points


def lottery(segments, points):
    START, END, POINT = 1,2,3
    data = []
    result = [0] * len(points)
    for start, end in segments:
        data.append((start, START))
        data.append((end, END))
    for position, point in enumerate(points):
        data.append((point, POINT, position))
    data.sort(key=lambda x: x[0])
    open_segments = 0
    for item in data:
        if item[1] == START:
            open_segments += 1
        elif item[1] == END:
            open_segments -= 1
        elif item[1] == POINT:
            result[item[2]] = open_segments
    return result



if __name__ == '__main__':
    # print(lottery([(0,5), (7,10)], [1,6,11]))  # 1 0 0
    # print(lottery([(-10, 10)], [-100, 100, 0]))  # 0 0 1
    # print(lottery([(0,5), (-3,2), (7,10)], [1,6]))  # 2 0
    print(sum(lottery(*dataset())))