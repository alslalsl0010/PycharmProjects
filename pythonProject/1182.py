import sys


5, def dfs(idx, total):
    global cnt

    if idx >= n:
        return
    total += l[idx]
    if total == s:
        cnt += 1

    dfs(idx+1, total)
    dfs(idx+1, total-l[idx])


input = sys.stdin.readline

n, s = map(int, input().split())
l = list(map(int, input().split()))
cnt = 0
dfs(0, 0)
print(cnt)
