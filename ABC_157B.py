import itertools
import bisect

def main():
    a = [list(map(int, (input().split()))) for _ in range(3)]
    n = int(input())
    ans = []
    for i in range(n):
        m = int(input())
        for j in range(3):
            for k in range(3):
                if a[j][k] == m:
                    ans.append((j,k))
    #print(ans)
    if (0,0) in ans and (1,1) in ans and (2,2) in ans:
        print("Yes")
    elif (0,0) in ans and (0,1) in ans and (0,2) in ans:
        print("Yes")
    elif (1,0) in ans and (1,1) in ans and (1,2) in ans:
        print("Yes")
    elif (2,0) in ans and (2,1) in ans and (2,2) in ans:
        print("Yes")
    elif (0,0) in ans and (1,0) in ans and (2,0) in ans:
        print("Yes")
    elif (0,1) in ans and (1,1) in ans and (2,1) in ans:
        print("Yes")
    elif (0,2) in ans and (1,2) in ans and (2,2) in ans:
        print("Yes")
    elif (0,2) in ans and (1,1) in ans and (2,0) in ans:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()