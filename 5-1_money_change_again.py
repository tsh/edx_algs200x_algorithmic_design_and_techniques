def change_money(money):
    coins = [1,3,4]
    min_num_coins = [0] + [float('inf')]*money
    for m in range(1, money+1):
        for coin in coins:
            if m >= coin:
                num_coins = min_num_coins[m-coin] + 1
                min_num_coins[m] = min(num_coins, min_num_coins[m])
    return min_num_coins[money]


if __name__ == '__main__':
    print(change_money(2))  # 2
    print(change_money(34))  # 9
    print(change_money(950))
