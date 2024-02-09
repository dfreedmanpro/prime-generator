from prime.utils import is_prime


def test_is_prime():
    assert is_prime(2)
    assert is_prime(5)
    assert not is_prime(9)
    assert is_prime(7901)
    assert not is_prime(7917)
