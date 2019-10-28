q = [{1, 3}, {1, 4}, {9, 5}, {5, 2}, {6, 5}, {3, 5}, {8, 9}, {7, 9}]
count = 0
while count != 10000:
    a = q.pop()
    for j in q:
        if len(j & a) != 0:
            j |= a
            count = 0
            break
    else:
        q = [a] + q
    if count > len(q):
        break
    count += 1
    print(count, q)
