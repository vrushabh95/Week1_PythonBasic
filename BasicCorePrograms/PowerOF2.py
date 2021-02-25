import sys

try:
    number = int(sys.argv[1])
    if 0 <= number < 31:
        for i in range(number + 1):
            result = (2**i)
            print(result)
    else:
        print('Enter proper value')
except:
    print("please provide command line argument")
