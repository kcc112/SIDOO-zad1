from utils.eval_math_fn import eval_math_fn
from utils.plot.marker import mark_interval, mark_point


def bisection(plot, fn, epsilon, a, b, iter_count):
    interval_start = a
    interval_end = b

    mark_interval(plot, fn, interval_start, interval_end)

    for k in range(1, iter_count + 1):
        l = interval_end - interval_start
        x1 = interval_start + l / 4
        x2 = interval_end - l / 4
        xm = (interval_start + interval_end) / 2

        vfx1 = eval_math_fn(fn, {'x': x1})
        vfx2 = eval_math_fn(fn, {'x': x2})
        vfxm = eval_math_fn(fn, {'x': xm})

        if abs(interval_end - interval_start) <= 2*epsilon:
            print(f'Minimum: {xm}')
            break
        elif vfx1 < vfxm:
            interval_end = xm
        elif vfx2 < vfxm:
            interval_start = xm
        else:
            interval_start = x1
            interval_end = x2

        print(f'Przedział {k}: [{interval_start}, {interval_end}]')
        print(f'Przedział {k}: minimum: {xm}')

        mark_interval(plot, fn, interval_start, interval_end)

    mark_point(plot, fn, xm)
