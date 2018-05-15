def calculate(n):
    res = []
    curent_sum = 0
    candidate = 1
    while True:
        will_be_left = n - (curent_sum + candidate)
        if will_be_left > candidate:
            res.append(candidate)
            curent_sum += candidate
            candidate += 1
        else:
            res.append(n - curent_sum)
            break
    return len(res)


if __name__ == '__main__':
    assert calculate(6) == 3
    assert calculate(8) == 3
    assert calculate(2) == 1
    print(calculate(182414564))