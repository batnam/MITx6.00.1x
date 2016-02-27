__author__ = 'ThanhNam'
def modSwapSort(L):
    """ L is a list on integers """
    print "Original L: ", L
    for i in range(len(L)):
        for j in range(len(L)):
            if L[j] < L[i]:
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                print L
    print "modSwapSort L: ", L


def swapSort(L):
    """ L is a list on integers """
    print "Original L: ", L

    Counter = 0
    for i in range(len(L)):
        for j in range(i+1, len(L)):
            Counter += 1
            if L[j] < L[i]:
                Counter += 1
                # the next line is a short
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j]
                #print L
    print Counter
    print "swapSort L: ", L

L = [1,2,5,7,3,2]
print (modSwapSort(L))
print (swapSort(L))