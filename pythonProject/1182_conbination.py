from itertools import combinations
N, S = map(int, input().split())
num_list = list(map(int, input().split()))
cnt = 0
for i in range(1, N + 1):
    # (리스트, i) 1개로 부분수열 조합, 2개로 조합, 3개로 조합 4개, 5개까지 증가하면서 만듦
    for j in combinations(num_list, i):
        if sum(j) == S:  # 한번 부분수열 만들어질떄마다 sum 검사해서 주어진 sum과 맞는지 체크
            cnt += 1
print(cnt)
