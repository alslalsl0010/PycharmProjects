A, B = input().split()
C = int(input())

if (60 - int(B)) >= C:
    print(f'{int(A)} {int(B)+C}')
elif (int(B) + C) == 60:
    print(f'{int(A) + 1} 0')
else:
    print(f'{int(A) + 1} {(C - (60 - int(B)))}')
