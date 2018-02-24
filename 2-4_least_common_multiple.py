# Uses python3
import sys

def gcd(a, b):
    if a == 0 or b == 0:
        return max(a, b)
    return gcd(b, a%b)

def lcm(a, b):
    return (a*b) // gcd(a, b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm(a, b))

