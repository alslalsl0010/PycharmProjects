import sys
input = sys.stdin.readline


def dfs(idx, depth):

    if depth == 6:
        print(*answer)  # 괄호 뺴고 출력하기
        return

    for i in range(idx, K):  # idx 말고 if로 도는 것 주의
        answer.append(S[i])
        dfs(i + 1, depth + 1)
        answer.pop()


while (1):
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    K = arr[0]
    S = arr[1:]
    answer = []
    dfs(0, 0)
    print()
