def is_Prime(i):

    if i == 1:
        return 0

    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            return 0
    return 1


min, max = map(int, input().split())

for i in range(min, max+1):
    if is_Prime(i):
        print(i)
