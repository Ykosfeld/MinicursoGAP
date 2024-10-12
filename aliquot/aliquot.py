def divisors(n: int) -> int:
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            yield i

def sum_divisors(n: int) -> int:
    list_divisors = list(divisors(n))
    return sum(list_divisors)

def is_perfect(n: int) -> bool:
    if n == sum_divisors(n):
        return True
    else:
        return False

def is_friendly(n: int) -> int:
    m = sum_divisors(n)
    sum_m = sum_divisors(m)
    if sum_m == n:
        return m
    else:
        return 0
