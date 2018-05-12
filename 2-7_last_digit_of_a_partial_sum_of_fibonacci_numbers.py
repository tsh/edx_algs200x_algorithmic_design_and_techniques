# Uses python3
import sys


def fibonacci_partial_sum_naive(from_, to):
    prev, cur = 0, 1
    fibs = [prev, cur]
    sums = [prev, prev+cur]
    # patterns repeats after 60 digits
    for i in range(58):
        prev, cur = cur, cur + prev
        fibs.append(cur%10)
    mto = (to+1) % 60
    if mto > from_:
        res = sum(fibs[from_:]) + sum(fibs[:mto])
    else:
        res = sum(fibs[from_:mto])
    print(res)
    return res % 10


if __name__ == '__main__':
    # input = sys.stdin.read();
    # from_, to = map(int, input.split())
    # print(fibonacci_partial_sum_naive(from_, to))
    # assert fibonacci_partial_sum_naive(3, 7) == 1
    # assert fibonacci_partial_sum_naive(10, 10) == 5
    # assert fibonacci_partial_sum_naive(10, 200) == 2
    assert fibonacci_partial_sum_naive(1234, 12345) == 5