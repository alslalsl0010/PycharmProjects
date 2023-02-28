a, b = map(str, input().split())

a = "".join(reversed(a))
b = "".join(reversed(b))

print(max(int(a), int(b)))


# join 주소접근시 or 문자열 합치기 조인도 소트랑 같이
# b = [1, 23, 43, 2]
# b.sort()  b 자체를 정렬
# sorted(b) 정렬된 b 객체 (b는 변화 x)
