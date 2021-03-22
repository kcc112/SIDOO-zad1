from utils.eval_math_fn import eval_math_fn
from utils.plot.marker import mark_interval, mark_point


def bisection(plot, fn, delta, a, b, iter_count):
    start = a
    end = b

    mark_interval(plot, fn, start, end)
    x = 0

    for k in range(1, iter_count + 1):
        print(f'Przedział {k}: [{start}, {end}]')
        x = (start + end) / 2

        if abs(eval_math_fn(fn, {"x": x})) <= delta:
            print(f'Środek: {x}')
            break
        else:
            if eval_math_fn(fn, {"x": x}) * eval_math_fn(fn, {"x": start}) < 0:
                end = x
            else:
                start = x

        mark_interval(plot, fn, start, end)

    # root
    mark_point(plot, fn, end)

