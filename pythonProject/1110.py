import sys
input = sys.stdin.readline

N = int(input())
num = N
a = 0
b = 0
c = 0
count = 0

while 1:
    a = N // 10
    b = N % 10
    c = a + b
    N = (10 * b) + (c % 10)
    count += 1
    if N == num:
        print(count)
        break
