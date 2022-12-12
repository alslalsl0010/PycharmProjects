T = int(input())

for i in range(T):
    iter, character = map(str, input().split())
    for j in character: # 문자열 갯수
        for _ in range(int(iter)): # 반복 횟수
            print(j, end='')
    print()

# map은 형 지정할때만, map으로 str을 받아도 문자열 쪽 배열 생성,
# j만 써도 가능, rstrip()은 뒤에 붙은 개행문자 없애주는 것





