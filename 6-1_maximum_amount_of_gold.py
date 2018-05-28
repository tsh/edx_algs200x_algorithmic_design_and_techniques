def dataset():
    with open('data/6_1_knapsack.in') as f:
        weight, number_of_bars = map(int, f.readline().split())
        data = map(int, f.readline().strip().split())
    return weight, list(data)


def max_gold(weight, bars):
    memo = [[0] * (weight+1) for _ in range(len(bars)+1)]

    for i in range(1, len(bars)+1):
        for w in range(1, weight+1):
            if bars[i-1] <= w:
                empty_space = w - bars[i-1]
                memo[i][w] = max(bars[i-1] + memo[i-1][empty_space], memo[i-1][w])
            else:
                memo[i][w] = memo[i-1][w]
    return memo[i][w]


if __name__ == '__main__':
    print(max_gold(10, [1, 4, 8]))  # 9
    print(max_gold(*dataset()))