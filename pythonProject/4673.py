s = set(range(1, 10001))

for a in range(1, 10001):
    for b in str(a): # a = '1', '2'. '3', '4'
        a += int(b) # a = 1234 + 1 + 2 + 3 + 4
    s.discard(a)

for num in s:
    print(num) # set 함수 대괄호와 콤마 없이 출력하기 위함

# set함수, str, int 활용 방법