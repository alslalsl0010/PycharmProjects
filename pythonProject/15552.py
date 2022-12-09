import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    A, B = map(int, input().rstrip().split())
    print(A+B)

# split() 의 경우 ()괄호 안에 오는 문자를 대상으로 나눠서 입력값을 저장해주는데
# 디폴트는 띄어쓰기
# readline 함수가
# 3을 입력받으면
# 3\n까지 입력을 받아서
# rstrip을 이용하면 그 개행을 제거하고
# 입력을 받아줌