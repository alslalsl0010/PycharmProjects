def is_Prime(i):

    if i == 1:
        return 0

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return 0
    return 1


testCase = int(input())
cnt = 0
num = list(map(int, input().split()))

for i in num:
    if is_Prime(i):
        cnt += 1

print(cnt)
