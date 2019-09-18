from collections import Counter

n = int(input())
letters = [input() for _ in range(n)]

cnt = Counter(letters[0])

for i in range(1,n):
    cnt = cnt & Counter(letters[i])

int_list = sorted(cnt.items(), key=lambda x:x[0])

ans = ""
for key, val in int_list:
    ans += key*val
print(ans)