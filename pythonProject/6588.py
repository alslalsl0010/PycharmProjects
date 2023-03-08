import sys
input = sys.stdin.readline

is_Prime = list([False]*1000001)

is_Prime[2] = True

for i in range(3, 1000001):
    error = 0
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            error += 1
            break

    if error == 0:
        is_Prime[i] = True

while (1):
    n = int(input())

    if n == 0:
        break

    for i in range(3, n):
        if is_Prime[i] == True:
            if is_Prime[n - i] == True:
                print(f'{n} = {i} + {n - i}')
                break

# 출력시 f함수 사용법 익히기
