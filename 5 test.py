from __future__ import division

# Use for, split(), and if to create a Statement that will print out words that start with 's':

st = 'Print only the words that start with s in this sentence'
x = st.split(' ')
for x in x:
    if x[:1] == 's':
        print x

for word in st.split():
    if word[0] == 's':
        print word

# Use range() to print all the even numbers from 0 to 10.

x = range(0, 10, 2)
print x

# Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3.

x = [x for x in range(50) if x % 3 == 0]

print x

# Go through the string below and if the length of a word is even print "even!"


st = 'Print every word in this sentence that has an even number of letters'
x = st.split()

for x in x:
    if len(x) % 2 == 0:
        print x + '  even'
    else:
        print x

'''
Write a program that prints the integers from 1 to 100.
But for multiples of three print "Fizz" instead of the number, 
and for the multiples of five print "Buzz". For numbers 
which are multiples of both three and five print "FizzBuzz".
'''

for x in xrange(1,101):
    if x % 3 == 0 and x % 5 == 0:
        print 'fizzBuzz'
    elif x % 3 == 0:
        print 'fizz'
    elif x % 5 == 0:
        print 'buzz'
    else:
        print x

# Use List Comprehension to create a list of the first letters of every word in the string below:

st = 'Create a list of the first letters of every word in this string'
print [word[0] for word in st.split()]