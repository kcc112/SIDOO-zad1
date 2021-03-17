from utils.eval_math_fn import eval_math_fn


def bisection(plot, fn, delta, a, b, iter_count):
    start = a
    end = b

    plot.scatter(start, eval_math_fn(fn, {"x": start}), color='blue')
    plot.scatter(end, eval_math_fn(fn, {"x": end}), color='blue')
    x = 0

    for k in range(1, iter_count):
        x = (start + end) / 2

        if abs(eval_math_fn(fn, {"x": x})) <= delta:
            print((start + end) / 2)
            break
        else:
            if eval_math_fn(fn, {"x": x}) * eval_math_fn(fn, {"x": start}) < 0:
                end = x
            else:
                start = x

        plot.scatter(start, eval_math_fn(fn, {"x": start}), color='blue')
        plot.scatter(end, eval_math_fn(fn, {"x": end}), color='blue')

    # root
    plot.scatter(x, eval_math_fn(fn, {"x": end}), color='red')
