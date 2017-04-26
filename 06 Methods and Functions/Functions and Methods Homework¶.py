# Write a function that computes the volume of a sphere given its radius.
import math
import string


def vol_sphere(r):
    return (4.0 / 3) * math.pi * r ** 3


print vol_sphere(3)


# Write a function that checks whether a number is in a given range (Inclusive of high and low)

def ran_bool(num, low, high):
    return low < num < high


print ran_bool(3, 1, 10)


def ran_bool2(num, low, high):
    return num in range(low, high + 1)


print ran_bool2(3, 1, 10)


# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def up_low(s):
    d = {'upper': 0, 'lower': 0}
    for c in s:
        if c.isupper():
            d['upper'] += 1
        elif c.islower():
            d['lower'] += 1
        else:
            pass
    print 'No. of Upper case characters : {}'.format(d['upper'])
    print 'No. of lower case characters : {}'.format(d['lower'])


s = 'Hello Mr. Rogers, how are you this fine Tuesday?'

up_low(s)


# Write a Python function that takes a list and returns a new list with unique elements of the first list.

def unique_list(l):
    print list(set(l))


unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])


def unique_list2(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    print x


unique_list2([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5, 6])


# Write a Python function to multiply all the numbers in a list.

def multiply(numbers):
    m = 1
    for c in numbers:
        m *= c
    print m


multiply([1, 2, 3, -4])


# Write a Python function that checks whether a passed string is palindrome or not.

def palindrome(s):
    s = s.lower()
    print s == s[::-1]


palindrome('Sore was I ere I saw Eros')


def ispangram(str1):
    alphabet = string.ascii_lowercase
    alphaset = set(alphabet)
    return alphaset <= set(str1.lower())


print ispangram("The quick brown fox jumps over the lazy dog")


# x = raw_input('do u?: ')
# print x