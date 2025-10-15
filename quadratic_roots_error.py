import math
from math import sqrt

def quadratic_roots(a, b, c):
    discriminant = b**2 - 4*a*c
    
    if discriminant >= 0:
        x1 = (-b + sqrt(discriminant)) / (2*a)
        x2 = (-b - sqrt(discriminant)) / (2*a)
    elif discriminant < 0:
        raise ValueError("The equation have not reel root")
    return x1, x2



print("This program solves ax^2 + bx + c = 0")

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

x1, x2 = quadratic_roots(a, b, c)

print(f"The solutions are: x1 = {x1}, x2 = {x2}")
