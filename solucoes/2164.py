n = int(input())
f = (((1 + 5 ** (1 / 2)) / 2) ** n - ((1 - 5 ** (1 / 2)) / 2) ** n) / 5 ** (1 / 2)
print("{:.1f}".format(f))
