import sys
sys.setrecursionlimit(10**7)


def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


input = sys.stdin.readline
n = int(input())
num_list = []

for i in range(n):
    m = int(input())
    num_list.append(m)
num_list.sort()


s = []

for i in range(n - 1):
    s.append(num_list[i + 1] - num_list[i])

temp = s[0]
for i in range(len(s) - 1):
    temp = gcd(temp, s[i + 1])

answer = set()
answer.add(temp)
for i in range(2, int(temp ** 0.5) + 1):  # temp가 6이면 3도 안돎
    if temp % i == 0:
        answer.add(i)  # 이것만 출력하면 6의 약수 했을떄 2만나오고 3이 안나옴
        answer.add(temp // i)
answer.add(temp)
print(*sorted(answer))
# .sort()는 리스트에만 사용가능 - 정렬 후 리스트에 정렬한 값 저장 ,set 함수 X
# sorted()는 리스트외에도 가능 set함수에도 가능
