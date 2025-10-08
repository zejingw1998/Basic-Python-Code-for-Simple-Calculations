import numpy 

# We defined the sequence a_n
def a(n):
    return (-1)**n

def cesaro_mean(N):
    a_values = [a(n) for n in range(N)]
    s_values = [sum(a_values[:k+1]) for k in range(N)] 
    if N == 1: 
        return s_values[0]
    S_N = (1/N-1)*sum(s_values[:N-1])
    return S_N 

print(f"{'N':>5} {'S_N':>10}")
print("-" * 15)
for N in [1, 2, 3, 4, 5, 10, 50]:
    print(f"{N:>5} {cesaro_mean(N):>10.4f}")


