def fibonacci(n):
    if n ==1 or n ==2:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonacci(n-1)+ fibonacci(n-2)


def gcd(a,b):
    while b > 0:
        (a, b) = (b, (a %b))
    return a


def compareTO(s1,s2):
    if len(s1) < len(s2):
        return -1
    elif len(s1) == len(s2):
        return 0
    else:
        len(s1) > len(s2)
        return 1
    return compareTO(s1[1:], s2[1:])

if __name__ == "__main__":
    print 'Fibonacci Result : %s ' % (fibonacci(20))
    print 'GCD Result : %s ' % (gcd(20, 30))
    print 'Compare To Result : %s' % (compareTO('is211', 'is211-part1'))


