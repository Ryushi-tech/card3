A = tuple(bisect.bisect_left(Asort, x) for x in A)

Y_rank = {z: i for i, z in enumerate(sorted(Y), 1)}