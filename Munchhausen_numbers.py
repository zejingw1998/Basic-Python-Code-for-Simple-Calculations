def is_munchhausen(n):
    """Check if a number n is a Münchhausen number."""
    if n <= 0:
        return False

    digits = [int(d) for d in str(n)]
    total = 0

    for d in digits:
        # Convention: 0^0 = 0
        if d == 0:
            total += 0
        else:
            total += d ** d

    return total == n



for num in range(1, 1_000_000):
    if is_munchhausen(num) and num != 1:
        print(num)
