from utils.eval_math_fn import eval_math_fn
from utils.nth_fibonacci_number import nth_fibonacci_number
from utils.plot.marker import mark_interval, mark_point


def get_n(b, a, E, n=2):
    if nth_fibonacci_number(n) > (b - a) / E:
        return n
    return get_n(b, a, E, n + 1)


def fibonacci(plot, fn, delta, a, b):
    n = get_n(b, a, delta)
    c = a + nth_fibonacci_number(n - 2) / nth_fibonacci_number(n) * (b - a)
    d = a + nth_fibonacci_number(n - 1) / nth_fibonacci_number(n) * (b - a)

    fc = eval_math_fn(fn, {"x": c})
    fd = eval_math_fn(fn, {"x": d})

    k = 1
    while n > 2:
        print(f'Iteracja: {k}, n: {n}, a: {a}, b: {b}, c: {c}, d: {d}')
        k += 1

        n -= 1
        mark_interval(plot, fn, a, b)
        if fc < fd:
            b = d
            d = c
            fd = fc
            c = a + nth_fibonacci_number(n - 2) / nth_fibonacci_number(n) * (b - a)
            fc = eval_math_fn(fn, {"x": c})
        else:
            a = c
            c = d
            fc = fd
            d = a + nth_fibonacci_number(n - 1) / nth_fibonacci_number(n) * (b - a)
            fd = eval_math_fn(fn, {"x": d})

    minimum = (a + b) / 2
    mark_point(plot, fn, minimum)

    print(f'Wynik: min: {minimum}, liczba iteracji: {k - 1}')
