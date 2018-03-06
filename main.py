def isPrime(num):
    if num < 4:
        return True
    for x in range(2, int(num/2)+1):
        if num % x is 0:
            return False
    return True


def isPrimeRoot(g, p):
    if g**(p-1) != 1 % p:
        return False
    for L in range(1, p-2):
        if g**L == 1 % p:
            return False
    return True


p = int(input("Enter a prime number (p): "))
while not isPrime(p):
    p = int(input("p isn't prime. Enter a prime number: "))

g = int(input("Enter a prime number (g): "))
while not isPrime(g) or not isPrimeRoot(g, p):
    if not isPrime(g):
        g = int(input("g isn't prime. Enter a prime number: "))
    else:
        g = int(input("g isn't a primitive root. Enter a primitive root: "))

x = int(input("Select an (x) between 1 to p-1 (non-inclusive): "))
while x < 2 or x > p-2:
    x = int(input("x is not in range between 1 and p-1. Enter a correct value: "))

y = g**x % p
print(f"y = {y}")

print(f"The open key (p, g, y) is ({p}, {g}, {y})")
print(f"The closed key K(c) is {x}")

m = int(input("Enter a message digit in range 0 to p-1: "))
while m < 0 or m > p-1:
    m = int(input("The message wasn't in range 0 to p-1. Enter a correct value: "))


