def fac(n):
    if n == 0:
        return 1
    return fac(n - 1) * n

n = int(input('введите число'))
print(fac(n))