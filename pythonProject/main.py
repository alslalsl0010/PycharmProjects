T = int(input())
n = 0

for i in range(1, T+1):
    arr = list(map(int, input().split()))
    for each in arr:
        if each % 2 == 1:
            n += each
    print (f"#{i} {n}")
    n = 0




