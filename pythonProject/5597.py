std = [i for i in range(1, 31)]

for _ in range(28):
    n = int(input())
    std.remove(n)

print(min(std))
print(max(std))

# 30개중에 28명이면 딱 2명 남으므로 출석번호중 가장 작은 것 출력하면 남는건 max다
