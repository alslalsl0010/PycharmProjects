T = int(input())
n = 0
for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    for i in arr:
        n += i
    n = n / len(arr)
    print(f"#{test_case} {round(n)}")
    n = 0

