def collatz(n:int) -> int:
    if n % 2 == 0:
        return n // 2
    else:
        return (3 * n) + 1

def nr_steps(n:int) -> int:
    k = 0
    while n != 1:
        k += 1
        n = collatz(n)
    return k

print(nr_steps(4))
