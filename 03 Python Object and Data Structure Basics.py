from __future__ import division

'''
Number
number
'''
print 3 / 2
print 3 ** 2
print 4 ** .5
a = 5
a = a + a
print a

'''
String
'''

print "this's string"
print "this's string\n new line"
print len('hello world')

x = 'Insert another string with curly brackets-- {}'.format('The inserted string')
print x

x = "this is one: {a} this is 2: {a} this is two point 5 :{c}".format(a=1, b="two", c=2.5)
print x

hello = 'hello'
print hello[3]
s = 'hellow world ewe'
print s.split()
print s.split('w')

# my lsit
'''
list
'''

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print my_list[:3]
print my_list[3:]
print my_list * 2
my_list = my_list + ['new Add']
print my_list

my_list.append('new append')

print my_list

print my_list.pop()
print my_list.pop(3)
print my_list

my_list.reverse()
print my_list
my_list.sort()

print my_list

l_1 = [1, 2, 3]
l_2 = [4, 5, 6]
l_3 = [7, 8, 9]

matrix = [l_1, l_2, l_3]
print matrix
print matrix[0][2]

'''
Dictionary
'''
my_dist = {'key1': 'value1', 'key2': 'value2'}
print my_dist

print my_dist['key1']
print my_dist['key1'][::-1].upper()
d = {}
print d
d['animal'] = 'dog'
d['Ans'] = 23
print d

nestedDec = {'k1': d, 'k2': my_dist, 'k3': {'k4': 5, 'k6': {'k7': 25}}}
print nestedDec
print nestedDec['k3']['k6']['k7'] + 10

print nestedDec.keys()
print nestedDec.values()
print nestedDec.items()
print nestedDec['k3']['k6'].values()

'''
Tuples
'''
t = ('one', 2, 3, 3)
print t

print t.index('one')
print t.count(3)

'''
file
'''

f = open('text.txt')

print f.read()
print f.read()
f.seek(0)
print f.read()
f.seek(0)
print f.readlines()

# myfile = open('results.txt', 'a')
# myfile.write('Hello, world!\n')
# myfile.write('Hello, world! bd\n')
# myfile.close()


for line in open('results.txt'):
    print line

'''
sets
'''

x = set()
print x

x.add(1)
print x

l = [3, 3, 9, 3, 3, 3, 3, 1, 2, 3, 4, 5, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5]
print set(l)

'''
booleans
'''

print 1 > 3

print 0.1 + 0.2 - 0.3
print 0.1 + 0.2 == .3

print 1 < 2
print 1 < 2 < 3
print 1 < 2 > 3
print 1 < 2 and 2 < 3
print 1 < 2 or 2 > 3
