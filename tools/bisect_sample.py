import bisect
a = [0,1,2,3,4,5,6,7,8,9]
a.insert(bisect.bisect(a, 3.5), 3.5)
print(a)