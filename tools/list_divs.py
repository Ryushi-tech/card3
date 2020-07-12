def list_divs(x):
    divs = []
    for y in range(1, int(x ** 0.5) + 1):
        if x % y == 0:
            divs.append(y)
            if y != x // y:
                divs.append(x // y)
    divs.sort()
    return divs