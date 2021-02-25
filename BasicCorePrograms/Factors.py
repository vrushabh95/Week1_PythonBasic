import math

def is_prime(number):
    sqrt_number = int(math.sqrt(number))
    for i in range(2, sqrt_number + 1):
        if number % i == 0:
            return False
    else:
        if number == 1:
            return False
        else:
            return True
def calc_prime_factors(number):
    prime_factors = []
    i = 2
    while i * i <= number:
        if number % i == 0 and is_prime(i):
            prime_factors.append(i)
        i += 1
    return prime_factors

number = int(input("Enter number"))
prime_factors = calc_prime_factors(number)
print(f"prime factors of {number} are {prime_factors}")