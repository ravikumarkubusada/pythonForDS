def findHCF(a, b):
    """ This fucction accepts two numbers and returns the HCF"""
    smaller = a if b>a else b
    print('smaller number is =', smaller)
    hcf = 1
    for i in range(1, smaller):
        if (a%i ==0) and (b%i == 0):
            hcf = i
    return hcf

number1 = 20
number2 = 10

print(findHCF.__doc__) #pritns the documentation

print('The HCF of number {0} and {1} is = {2}'.format(number1, number2, findHCF(20,10)))


