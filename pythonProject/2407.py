def factorial(n):
    num = 1
    for i in range(2, n+1):
        num *= i
    return num


n, m = map(int, input().split())
print(factorial(n) // factorial(n-m) * factorial(m))

# 꾸준히 진행하자
