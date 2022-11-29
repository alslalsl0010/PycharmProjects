arr = list(input().rstrip())

for i in arr:
    print(ord(i)-64, end=" ")




    # print(arr) -> ['a', 'b']
    # print(*arr) -> a b
    # print (, end = " ") -> 출력시 개행 없애주고 띄어쓰기 후 출력