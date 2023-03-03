num = int(input())

groupWord = 0

for i in range(num):
    word = str(input())
    error = 0

    for i in range(len(word) - 1): # word 범위 조심
        if word[i] != word[i+1]:
            new_word = word[i+1:]
            if new_word.count(word[i]) > 0: # 1번지 값은 이미 위에서 비교했으니까 1~ 끝까지 저장 후 맨 첫번쨰랑 비교해서 같은 거 있는지 확인
                error += 1
    if error == 0:
        groupWord += 1

print(groupWord)

