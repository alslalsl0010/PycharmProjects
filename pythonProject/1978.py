testCase = int(input())
answer = 0

num = list(map(int, input().split()))

for i in num:
    if i == 1:
        continue

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break

    else:
        answer += 1

print(answer)
