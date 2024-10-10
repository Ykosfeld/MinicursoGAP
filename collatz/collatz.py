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

def max_nr_steps(n_max: int) -> list[int, int]:
    max_steps = 0
    max_n = 1

    for n in range(1, n_max + 1):
        n_steps = nr_steps(n)
        #print(n, steps)
        if n_steps >= max_steps:
            max_steps = n_steps
            max_n = n

    return [max_n, max_steps]

print(max_nr_steps(1000))
