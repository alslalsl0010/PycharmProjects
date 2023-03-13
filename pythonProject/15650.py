import sys


def dfs(idx):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(idx, n + 1):
        if i not in answer:
            answer.append(i)
            dfs(i + 1)  # 조심 idx 아님
            answer.pop()


input = sys.stdin.readline

n, m = map(int, input().split())
answer = []
dfs(1)
