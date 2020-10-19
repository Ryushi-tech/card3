n = 1200
s = "AGCT" * n
with open("input2.txt", "w") as f:
    f.write(str(4 * n) + " " + s)
