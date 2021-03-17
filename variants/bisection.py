from math import sin, pow, sqrt

def bisection(plot, fn, delta, a, b, iter_count):
    start = a
    end = b

    plot.scatter(start, eval(fn, {"x": start, 'sin': sin, 'sqrt': sqrt, 'pow': pow}), color='blue')
    plot.scatter(end, eval(fn, {"x": end, 'sin': sin, 'sqrt': sqrt, 'pow': pow}), color='blue')
    x = 0

    for k in range(1, iter_count):
        x = (start + end) / 2

        if abs(eval(fn, {"x": x, 'sin': sin, 'sqrt': sqrt, 'pow': pow})) <= delta:
            print((start + end) / 2)
            break
        else:
            if eval(fn, {"x": x, 'sin': sin, 'sqrt': sqrt, 'pow': pow}) * eval(fn,
                                                                               {"x": start, 'sin': sin, 'sqrt': sqrt,
                                                                                'pow': pow}) < 0:
                end = x
            else:
                start = x

        plot.scatter(start, eval(fn, {"x": start, 'sin': sin, 'sqrt': sqrt, 'pow': pow}), color='blue')
        plot.scatter(end, eval(fn, {"x": end, 'sin': sin, 'sqrt': sqrt, 'pow': pow}), color='blue')

    # root
    plot.scatter(x, eval(fn, {"x": end, 'sin': sin, 'sqrt': sqrt, 'pow': pow}), color='red')