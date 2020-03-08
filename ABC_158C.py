def main():
    n,m = map(int, input().split())
    ans = 100000
    for i in range(5*m, 15*m):
        if int(i * 0.08) == n and int(i * 0.1) == m:
          ans = min(ans,i)
    print(-1) if ans == 100000 else print(ans)

if __name__ == '__main__':
    main()