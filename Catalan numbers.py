import math

def catalan_number(n):
    return math.factorial(2 * n) // (math.factorial(n + 1) * math.factorial(n))

# Print the first 10 Catalan numbers 
for n in range(10):
    print(f"C_{n} = {catalan_number(n)}")
