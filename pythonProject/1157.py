word = input().lower() # 소문자 word = mississipi
word_without_iter = list(set(word)) # set함수로 중복제거 ['m', 'i', 's', 'p']
cnt = []

for i in (word_without_iter):  # i = m, i, s, p
    count = word.count(i)
    cnt.append(count) # cnt = [4, 4, 1, 1]

if cnt.count(max(cnt)) >= 2:
    print('?')

else:
    print(word_without_iter[cnt.index(max(cnt))].upper())

# cnt.count / cnt.indew / lower / upper / 리스트 참조시 arr[]  주의
