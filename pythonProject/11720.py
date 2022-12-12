import math

N = int(input())
num = int(input())
cnt = 0

for i in range(N, 0, -1):
    cnt += num // pow(10, i)
    num = num % pow(10, i)
cnt += num

print(cnt)