N = int(input())
sum = 0
arr = list(map(int, input().split()))

M = max(arr)

for i in range(len(arr)):
    arr[i] = arr[i] / M * 100
    sum += arr[i]

print(sum / N)

# range(값)이 5면 0~4까지 돌아서 총 5번이 된다.
# range(0,5) 와 같은 것


