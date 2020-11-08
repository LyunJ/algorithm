
n = int(input())
R, G, B = [0 for i in range(n)], [0 for i in range(n)], [0 for i in range(n)]
for i in range(n):
    R[i], G[i], B[i] = map(int, input().split())

D = [[0]*3]*n


D[0][0] = R[0]
D[0][1] = G[0]
D[0][2] = B[0]


for i in range(1, n):
    D[i][0] = min(D[i-1][1], D[i-1][2]) + R[i]
    D[i][1] = min(D[i-1][0], D[i-1][2]) + G[i]
    D[i][2] = min(D[i-1][0], D[i-1][1]) + B[i]

ans = min(D[n-1][0], D[n-1][1], D[n-1][2])
print(ans)
