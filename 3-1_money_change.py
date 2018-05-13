from math import floor


def change(n):
    total = 0
    coins = [10, 5, 1]
    coin_index = 0
    money = n
    while money > 0 and coin_index < len(coins):
        total += floor(money / coins[coin_index])
        money = money % coins[coin_index]
        coin_index += 1
    return total

if __name__ == '__main__':
    print(change(997))