from itertools import permutations

# 입력
N = int(input())

# 순열 구하기( 1~ 3 , 몇개씩 순열로 만들것인지)
res = permutations(range(1, N+1), N)

# 출력
for perm in res:
    for i in perm:
        print(i, end=" ")
    print()
