num1, num2 = map(int, input().split())
cnt = 0


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


print(gcd(num1, num2))
print(num1 * num2 // gcd(num1, num2))
# 유클리드 호제법 - 최대공약수 : b와 a % b의 최대공약수를 구하면 된다 (24, 18)->(18, 6)->(6, 0)
#                 - 최대공배수 : a * b // gcd
