primeNum = list([False] * 246913)
primeNum[1] = True

while (1):
    is_prime = 0
    num = int(input())

    if num == 0:
        break

    for i in range(num + 1, num * 2 + 1):
        error = 0
        if primeNum[i] == True:
            is_prime += 1
            continue

        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                error += 1
                break

        if error == 0:
            primeNum[i] = True
            is_prime += 1

    print(is_prime)
