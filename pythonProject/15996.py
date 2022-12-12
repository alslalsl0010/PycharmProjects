import sys
input = sys.stdin.readline
cnt = 0

N, A = map(int, input().split())
X = A

while A <= N:
    cnt += N // A
    A *= X

print(cnt)

# factorial 인데 불구하고 N 값을 기준으로 2, 2^2, 2^3 순으로 크게 만들면서 N을 넘지 않는지 확인



