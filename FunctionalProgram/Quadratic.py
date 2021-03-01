import cmath

try:
    a = int(input("enter the value of 'a':"))
    b = int(input("enter the value of 'b':"))
    c = int(input("enter the value of 'c':"))
    delta = (b ** 2) - (4 * a * c)

    root1 = (-b - cmath.sqrt(delta)) / (2 * a)
    root2 = (-b + cmath.sqrt(delta)) / (2 * a)

    print('The solution are {0} and {1}'.format(root1, root2))
except ZeroDivisionError:
    print("enter greater than zero")

