# A = tuple(bisect.bisect_left(Asort, x) for x in A)

# sy = sorted({p for p, a, b in PAB})
# compress = {z: i for i, z in enumerate(sy)}


def coordinateCompression(arr):
    sar = sorted(arr)
    mp = {z: i for i, z in enumerate(sar, 1)}
    res = [mp[x] for x in arr]
    return res


B = [1, 30, 70, 2, 60, 40, 50]
D = coordinateCompression(B)
print(D)
