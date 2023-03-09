import sys
input = sys.stdin.readline


def dfs(idx, total):
    global cnt
    if idx == N:
        return
    total += num_list[idx]
    if total == S:
        cnt += 1
    dfs(idx + 1, total)
    dfs(idx + 1, total - num_list[idx])


N, S = map(int, input().split())
num_list = list(map(int, input().split()))
cnt = 0
dfs(0, 0)
print(cnt)
