lis = list(map(int,input().split()))
if lis[0] == lis [1] and lis[0] != lis[2]:
    print("Yes")
elif lis[1] == lis[2] and lis[1] != lis[0]:
    print("Yes")
elif lis[0] == lis[2] and lis[2] != lis[1]:
    print("Yes")
else:
    print("No")