import sys
input = sys.stdin.readline

def main():
    n = int(input())
    s = input()
    R = 0
    G = 0
    B = 0

    for i in range(n):
        if s[i] == "R":
            R += 1
        elif s[i] == "G":
            G += 1
        else:
            B += 1

    res = R*G*B
    for i in range(n - 2):
        for j in range(i + 1, i + 1 + (n - 1 - i) // 2):
            k = j + (j - i)
            if s[i] != s[j] != s[k] != s[i]:
                res -= 1
    print(res)
if __name__ == '__main__':
    main()
