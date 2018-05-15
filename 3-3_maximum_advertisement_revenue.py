import operator
from functools import reduce

def dataset():
    with open('data/3_3_dot_product20180216.in') as f:
        _ = f.readline()
        seq1 = map(int, f.readline().split())
        seq2 = map(int, f.readline().split())
    return list(seq1), list(seq2)


def best_ads(seq1, seq2):
    seq1.sort(reverse=True)
    seq2.sort(reverse=True)
    return reduce(operator.add, map(operator.mul, seq1, seq2))

if __name__ == '__main__':
    assert best_ads([1,3,-5], [-2,4,1]) == 23
    print(best_ads(*dataset()))