fibonacci_numbers = [0, 1]


# Uses memoization for previously calculated fibonacci numbers
def nth_fibonacci_number(n):
    if n < 0:
        print(f'Błąd - liczba n: {n} < 0')
    else:
        if n >= len(fibonacci_numbers):
            for i in range(2, n + 1):
                if i >= len(fibonacci_numbers):
                    fibonacci_numbers.append(fibonacci_numbers[i - 1] + fibonacci_numbers[i - 2])

        return fibonacci_numbers[n]
