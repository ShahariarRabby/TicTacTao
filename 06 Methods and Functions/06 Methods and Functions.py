"""
Method
"""
l = [1, 2, 3, 4, 5]
print l
l.append(6)
# append is a method
print l
# count is a method
print l.count(3)

# To know about some built in method
print help(l.count)

"""
Function
"""


def name_of_function(arg1, arg2):
    print 1
    pass


name_of_function(1, 2)


def my_addition_function(arg1, arg2):
    """
        this will print the sum of two number
    """
    print arg1 + arg2


my_addition_function(2, 2)


def greeting(name):
    print "Hello " + name


greeting('Rabby')


def add_num(num1, num2):
    """
        this will return the sum of two number, this can be stored in a variable
    """
    return num1 + num2


x = add_num(1, 2)
print x


def is_prime(num):
    """
    
    :param num: Input a number 
    :return: this is prime or not
    """
    for n in range(2, num):
        if num % n == 0:
            print "Not a prime number"
            break
    else:
        print "This is a prime"


is_prime(13)


def pi():
    return 22 / 7


"""
Lambda
"""

even = lambda num: num % 2 == 0

print even(2)

rev = lambda s: s[::-1]
print rev('Hello world')


