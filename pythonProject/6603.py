from itertools import combinations
import sys
input = sys.stdin.readline

while (1):
    num = list(map(int, input().split()))

    if 0 in num:
        break

    num.pop(0)

    for i in combinations(num, 6):
        print(' '.join(map(str, i)))

    print()
