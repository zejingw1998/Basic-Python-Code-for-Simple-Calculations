from math import exp

def population(t, k, B, C):
    return B / (1 + C * exp(-k * t))

if __name__ == "__main__":
    # parameters from Problems 2.3 & 3.7
    B = 50_000         # carrying capacity
    k = 0.2            # per hour
    N0 = 5_000         # initial population at t=0
    C = B / N0 - 1     # = 9

    n = 12
    t0, T = 0.0, 48.0
    dt = (T - t0) / n

    print(f"{'t (h)':>6} | {'N(t)':>12}")
    print("-" * 22)
    for i in range(n + 1):          
        t = t0 + i * dt
        N = population(t, k, B, C)
        print(f"{t:6.1f} | {N:12.2f}")
