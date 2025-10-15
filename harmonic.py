def harmonic_series(x, N):
    total = 0.0
    for n in range(1, N + 1):
        total += (x ** n) / n
    return total


print("This program approximates f(x) = sum(x^n / n)")

x = float(input("Enter x: "))
N = int(input("Enter N: "))

result = harmonic_series(x, N)
print(f"f_{N}({x}) = {result}")
