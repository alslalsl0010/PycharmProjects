C = int(input())

for i in range(C):
    sum = 0
    cnt = 0  # 평균넘는 사람 카운트
    arr = list(map(int, input().split()))
    num = arr[0]
    arr = arr[1:]

    for j in range(len(arr)):
        sum += arr[j] # 평균넘는 사람 카운트
    avg = sum / num

    for k in range(len(arr)):
        if arr[k] > avg:
            cnt += 1
    print('{:.3f}%'.format(cnt / num * 100))

# sum cnt 초기화 주의, arr 0번을 따로 저장하고 1~ arr 끝까지 앞으로 미는 문법 확인
