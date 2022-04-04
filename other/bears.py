def bears(n):
    if n == 42:
        return True
    elif n < 42:
        return False

    if n % 2 == 0:
        if (bears(n / 2)):
            return True
    if n % 3 == 0 or n % 4 == 0:
        ones = n % 10
        tens = (n // 10) % 10
        if (bears(ones * tens)):
            return True
    if n % 5 == 0:
        if (bears(n - 42)):
            return True

    return False
