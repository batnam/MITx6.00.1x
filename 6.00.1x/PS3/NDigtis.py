__author__ = 'ThanhNam'
def ndigits( x ):
    x = abs(x)
    if x < 10:
        return 1
    return 1 + ndigits(x / 10)

print(ndigits(1231235655453));