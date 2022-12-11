arr = []

for i in range(9):
    a = int(input())
    arr.append(a)

print(max(arr))
print(arr.index(max(arr)) + 1)

#index 뽑아낼 때는 arr.index