from prime.generator import prime_generator


def test_prime_generator():
    gen = prime_generator(7900, 7920)
    assert list(gen) == [7901, 7907, 7919]


def test_prime_generator_with_inverse_range():
    gen = prime_generator(7920, 7900)
    assert list(gen) == [7901, 7907, 7919]
