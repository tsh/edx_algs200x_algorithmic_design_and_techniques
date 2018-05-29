def dataset():
    with open('data/6_2_souvenirs.in') as f:
        vs = []
        line = f.readline()
        while line:
            vals = map(int, f.readline().split())
            vs.append(list(vals))
            f.readline()
            line = f.readline()
    return vs


def partition_souvenirs(vs):
    sum_ = sum(vs)
    if sum_ % 3 != 0:
        return False

if __name__ == '__main__':
    print(partition_souvenirs([3,3,3,3]))  # 0
    print(partition_souvenirs([30]))  # 0
    print(partition_souvenirs([1,2,3,4,5,5,7,7,8,10,12,19,25]))  # 1