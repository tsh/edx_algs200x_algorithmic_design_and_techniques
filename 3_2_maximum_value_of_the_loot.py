def dataset():
    with open('data/3_2_loot.in') as f:
        n, capacity = map(int, f.readline().split())
        items = []
        for line in f.readlines():
            if len(line) < 2:
                # empty line
                continue
            value, weight = map(int, line.split())
            items.append((value, weight,))
    return capacity, items


def loot_value(capacity, items):
    items.sort(key=lambda x: x[0] / x[1], reverse=True)  # most valuable

    while capacity > 0:
        pass

if __name__ == '__main__':
    print(loot_value(50, [(60, 20), (100, 50), (120, 30)]))  #180