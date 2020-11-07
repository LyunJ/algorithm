n = int(input())
R = []
for i in range(n):
    up = 1
    down = 1
    a, b = input().split()
    a = int(a)
    b = int(b)

    if(a > b):
        R.append(0)
        continue

    for r in range(a):
        up = (b-r) * up
        down = (a - r) * down

    if (down == 0):
        R.append(0)
    else:
        R.append(int(up/down))


for i in range(n):
    print(R[i])
