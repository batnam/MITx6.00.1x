__author__ = 'ThanhNam'
s = 'gaoedum'
def countVowels(s):
    count = 0
    for letter in s:
        if letter in 'aeiou':
            count += 1
    print 'Number of vowels: ' + str(count)

countVowels(s)