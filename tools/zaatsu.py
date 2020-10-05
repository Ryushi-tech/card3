A = tuple(bisect.bisect_left(Asort, x) for x in A)

sy = sorted({p for p, a, b in PAB})
compress = {z: i for i, z in enumerate(sy)}
