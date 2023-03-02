a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = str(input())
for i in a:
    word = word.replace(i, '*')

print(len(word))


