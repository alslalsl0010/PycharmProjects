min, max = map(int, input().split())

for i in range(min, max + 1):
    if i == 1:
        continue

    for j in range(2, int(i ** 0.5) + 1): # 특정 수의 제곱근을 구해 그 제곱근까지의 약수를 구하면 소수 구할 수 ㅇ
        if i % j == 0:
            break;
    else:
        print(i)




