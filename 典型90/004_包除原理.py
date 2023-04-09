H, W = map(int, input().split())
A = [0 for i in range(H)]
for i in range(H):
    a = list(map(int, input().split()))
    A[i] = a

X = [0 for i in range(H)]
Y = [0 for i in range(W)]
for i in range(H):
    for j in range(W):
        X[i] += A[i][j]
        Y[j] += A[i][j]

for i in range(H):
    for j in range(W):
        print(X[i] + Y[j] - A[i][j], end=" ")
    print()
