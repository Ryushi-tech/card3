from card3.void.stop_watch import stop_watch

@stop_watch
def main():
    h, w = map(int, input().split())

    g = [list("#" * (w + 2))]
    for _ in range(h):
        g.append(["#"] + list(input()) + ["#"])
    g += [list("#" * (w + 2))]
    area = [[0] * (w + 2) for _ in range(h + 2)]

    for i in range(h + 2):
        cnt = 0
        for j in range(w + 2):
            if g[i][j] == "#":
                for k in range(j - cnt, j):
                    area[i][k] += cnt
                cnt = 0
            else:
                cnt += 1

    for i in range(w + 2):
        cnt = 0
        for j in range(h + 2):
            if g[j][i] == "#":
                for k in range(j - cnt, j):
                    area[k][i] += cnt
                cnt = 0
            else:
                cnt += 1

    res = 0
    for i in range(h + 2):
        for j in range(w + 2):
            res = max(res, area[i][j])
    print(res - 1)
if __name__ == '__main__':
    main()