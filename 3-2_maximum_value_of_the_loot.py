def dataset():
    with open('data/3_2_loot.in') as f:
        _, capacity = map(int, f.readline().split())
        items = []
        for line in f.readlines():
            if len(line) < 2:
                # empty line
                continue
            value, weight = map(int, line.split())
            items.append((value, weight,))
    return capacity, items


def calc_value(capacity, items):
    items.sort(key=lambda x: x[0] / x[1], reverse=True)  # most valuable

    loot_value = 0
    for value, weight in items:
        if capacity == 0:
            return loot_value
        take = min(capacity, weight)
        loot_value += take * (value/weight)
        capacity -= take
    return loot_value

if __name__ == '__main__':
    assert calc_value(50, [(60, 20), (100, 50), (120, 30)]) == 180
    print(calc_value(*dataset()))