from .utils import is_prime


def prime_generator(start: int, end: int):
    if start > end:
        start, end = end, start

    return (n for n in range(start, end + 1) if is_prime(n))
