a_list = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0
word = str(input())

for i in a_list: #ABC
    for j in i: #A
        for k in word:
            if k == j:
                time += a_list.index(i) + 3

print(time)