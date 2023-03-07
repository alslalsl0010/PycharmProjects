test_case = int(input())

is_prime = list([False] * 10001)
is_prime[2] = True

for i in range(3, 10001):
    error = 0
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            error += 1
            break
    if error == 0:
        is_prime[i] = True

for i in range(test_case):
    n = int(input())

    # 가장 차이 안나는 소수끼리 더해서 n이 나와야하니까 두 소수가 중간에 가까울 수록 서로 차이가 안난다는 아이디어
    for i in range(int(n / 2), 1, -1):  # 2로 나누고 거꾸로 돌려서 나오는 첫 소수를 채택
        if is_prime[i] == True:
            if is_prime[n - i] == True:
                print(i, end=' ')
                print(n - i)
                break

# for i in range(2,2, -1) 하면 2전까지로 되므로 for문 안 돌아감
