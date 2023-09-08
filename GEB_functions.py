def G(n):
    val = 0
    if n > 0:
        val = n - G(G(n-1))
    print(f"G({n}) = {val}")
    return val


def F(n):
    val = 1
    if n > 0:
        val = n - M(F(n-1))
    print(f"F({n}) = {val}")
    return val


def M(n):
    val = 0
    if n > 0:
        val = n - F(M(n-1))
    print(f"M({n}) = {val}")
    return val


def Q(n):
    val = 1
    if n > 2:
        val = Q(n-Q(n-1)) + Q(n-Q(n-2))
    print(f"Q({n}) = {val}")
    return val


Q(6)
