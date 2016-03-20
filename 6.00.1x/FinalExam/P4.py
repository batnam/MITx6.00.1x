__author__ = 'ThanhNam'
def getSublists(L, n):
    ll = []
    for i in range(len(L) - n + 1):
        sl = []
        for j in range(i, i + n):
            sl.append(L[j])
        ll.append(sl)
    return ll

def longestRun(L):
    cr = lr = 1
    i = 0
    while i < len(L) - 1:
        if L[i] <= L[i + 1]:
            cr += 1
            if cr > lr:
                lr = cr
        else:
            cr = 1
        i += 1
    return lr