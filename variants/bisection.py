from utils.eval_math_fn import eval_math_fn
from utils.plot.marker import mark_interval, mark_point, mark_unimodal_interval
from utils.is_unimodal import is_unimodal


def bisection(plot, fn, epsilon, a, b, iter_count):
    interval_start = a
    interval_end = b
    x = 0

    if is_unimodal(interval_start, interval_end, fn, 0.2):
        mark_unimodal_interval(plot, fn, interval_start, interval_end)

    mark_interval(plot, fn, interval_start, interval_end)

    for k in range(1, iter_count + 1):
        
        print(f'Przedział {k}: [{interval_start}, {interval_end}]')
        
        x = (interval_start + interval_end) / 2

        if abs(eval_math_fn(fn, {'x': x})) <= epsilon:
            print(f'Pierwiastek: {x}')
            break
        else:
            if eval_math_fn(fn, {'x': x}) * eval_math_fn(fn, {'x': interval_start}) < 0:
                interval_end = x
            else:
                interval_start = x
        
        mark_interval(plot, fn, interval_start, interval_end)

    mark_point(plot, fn, interval_end)
