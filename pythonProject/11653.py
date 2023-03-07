num = int(input())
cnt = num

for i in range(2, num + 1):  # num값은 포문에서 변하지 않도록 cnt변수 만들어서 나누고 남은 몫 계속 중간저장
    while (cnt % i == 0):
        cnt = cnt // i
        print(i)
    if cnt == 1:
        break
