T = int(input())

for test_case in range(1, T + 1):
    arr = list(map(int, input().split()))
    if arr[0] > arr[1]:
        print(f"#{test_case} >")
    elif arr[0] == arr[1]:
        print(f"#{test_case} =")
    else :
        print(f"#{test_case} <")