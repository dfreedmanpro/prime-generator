# Prime Number Generator

## Table of contents

- [Project overview](#project-overview)
- [How to setup](#how-to-setup)
- [How to run main program](#how-to-run-main-program)
- [How to run unit tests](#how-to-run-unit-tests)

## Project overview

Your task is to use test-driven development to implement a prime number generator that returns prime numbers in a given range (inclusive of the endpoints). You must implement the generator specified below. You may also create any other methods, interfaces and/or classes that you deem necessary to complete the project. You should also develop a small main program to drive your generator and to allow the user to specify the prime number range via the command line. To successfully complete the exercise, all unit tests must pass as well as provide 100% code coverage.

### Notes

- You may not use the isprime method from sympy, we want to see you implement a python generator that returns primes on your own.
- The code should handle inverse ranges such that 1-10 and 10-1 are equivalent.
- Ensure that you run a test against the range 7900 and 7920 (valid primes are 7901, 7907, 7919).

### Generator function signature

```python
def prime_generator(start:int , end:int)
```

### Primality checker signature 

```python
def is_prime(value:int) 
```

### Definition (from wikipedia):

In mathematics, a prime number (or a prime) is a natural number which has exactly two distinct natural number divisors: 1 and itself. The first twenty-six prime numbers are: 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101

## How to setup

### Install python

1. Install pyenv and python

Please follow the [pyenv installation guide](https://github.com/pyenv/pyenv#installation)

```shell
pyenv install 3.11.4
```

2. Install pyenv-virtualenv and create virtualenv

Please follow the [pyenv-virtualenv installation guide](https://github.com/pyenv/pyenv-virtualenv#installation)

```shell
pyenv virtualenv 3.11.4 drchrono-3.11.4
pyenv activate
```

3. Install Python packages

```shell
pip install -r requirements.txt
```

## How to run main program

```shell
python main.py
```

## How to run unit tests

```shell
pytest --cov=prime
```
