for _ in range(int(input())):
    n, k = map(int, input().split())
    W = list(map(int, input().split()))

    V = [0] * (50 + 1)
    V[0] = 1

    best = 0
    for i in range(k):
        if V[i] == 1:
            for j in W:
                V[i + j] = 1
                print(V,i,j,best)
                if i + j <= k:
                    best = max(best, i + j)
    print(best)