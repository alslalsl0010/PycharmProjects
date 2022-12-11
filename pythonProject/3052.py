arr = []

for i in range(10):
    num = int(input())
    arr.append(num % 42)

answer = set(arr)
print(len(answer))

# SET을 이용하여 중복 제거하기
# 집합 자료형은 크게 두가지 특징이 있다.

# 중복을 허용하지 않는다.
# 순서가 없다.

# set의 방식으로 중복을 제거할 경우, 순서가 뒤죽박죽 된다는 단점이 있다. 만약 순서를 지켜야 하는 경우, 반복문을 사용한다.
