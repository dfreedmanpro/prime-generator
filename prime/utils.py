def is_prime(value: int) -> bool:
    n = 2

    while n**2 <= value:
        if value % n == 0:
            return False
        n += 1

    return True
