primeNum = list([False] * 246913)  # 0부터 인덱스 생기니까 246912 인덱스 쓰려면 246913개 만들어야 함
primeNum[2] = True

for i in range(3, 246913):
    error = 0
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            error += 1
            break

    if error == 0:
        primeNum[i] = True

while (1):
    cnt = 0
    num = int(input())

    if num == 0:
        break

    for i in range(num + 1, num * 2 + 1):
        if primeNum[i] == True:
            cnt += 1
    print(cnt)

# 처음에 num 하나 들어올떄마다 그 부분만 소수 체크해서 바꿔주는 방식으로 했지만 오히려 시간초과
# 미리 다 소수 true 만들어 놓고 num 들어올 때 마다 그 조건에 소수 몇개 있는지만 체크
