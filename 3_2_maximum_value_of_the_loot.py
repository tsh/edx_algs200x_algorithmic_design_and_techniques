with open('data/3_2_loot.in') as f:
    n, capacity = map(int, f.readline().split())
    items = []
    for line in f.readlines():
        if len(line) < 2:
            # empty line
            continue
        value, weight = map(int, line.split())
        items.append((value, weight,))