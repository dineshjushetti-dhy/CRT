def sum_of_digits(n: int) -> int:
    """Return the sum of the digits of the given integer n."""
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n //= 10
    return total

if __name__ == '__main__':
    n = int(input())
    print(sum_of_digits(n))
