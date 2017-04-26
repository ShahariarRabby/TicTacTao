from __future__ import division

if 1 == 1:
    print "true"

x = False

if x:
    print "True"
else:
    print "false"

loc = 'Dhaka'

if loc == 'dhaka':
    print "dhaka"
elif loc == 'Dhaka':
    print 'Dhaka'
else:
    print 'none'

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for element in l:
    print element

suml = 0
for element in l:
    suml = suml + element

print suml

t = [(1, 2), (3, 4), (5, 6)]

for tup in t:
    print tup

for (t1, t2) in t:
    print t1

dic = {'k1': 1, 'k2': 2, 'k3': 3}

for k, v in dic.iteritems():
    print k, v

x = 0

while x < 10:
    print 'x is now: ', x
    x += 1
else:
    print 'all done'

x = 0

while x < 10:
    x += 1
    if x == 3:
        print "ok"
        break
    else:
        print 'go'

print range(0, 10, 2)

x = "hello"
print type(x)

x = range(1, 10)
print x
print type(x)

x = xrange(1, 10)
print x
print type(x)

lst = [x for x in xrange(0, 11)]
print lst

lst = [x**2 for x in xrange(0, 11)]
print lst

lst = [x for x in xrange(0, 11) if x % 2 == 0]
print lst
