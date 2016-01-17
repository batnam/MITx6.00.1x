__author__ = 'ThanhNam'
s = 'bolmiobobbb'
def countBob(s):
    count = 0
    for i in range(1, len(s) - 1):
        if s[i-1 : i+2] == 'bob':
            count += 1
    print 'Number of times bob occurs is:' + str(count)
countBob(s)
