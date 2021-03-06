def calculate_nth_harmonic(n):
    nth_harmonic = 0
    for i in range(1, n + 1):
        nth_harmonic += 1 / i
    return nth_harmonic


n = int(input("Enter a number"))
print(calculate_nth_harmonic(n))