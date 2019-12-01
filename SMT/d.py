import itertools

n = int(input())
lis = tuple(input())

ans = tuple(itertools.combinations(lis, 3))

result = []
for line in ans:
    if line not in result:
        result.append(line)
print(len(result))