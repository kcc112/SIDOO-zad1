from utils.eval_math_fn import eval_math_fn


def mark_interval(plot, fn, start, end):
    plot.scatter(start, eval_math_fn(fn, {'x': start}), marker="|", linewidths=2, c='black')
    plot.scatter(end, eval_math_fn(fn, {'x': end}), marker="|", linewidths=2, c='black')

def mark_unimodal_interval(plot, fn, start, end):
    plot.scatter(start, eval_math_fn(fn, {'x': start}), marker="x", linewidths=1, c='green')
    plot.scatter(end, eval_math_fn(fn, {'x': end}), marker="x", linewidths=1, c='green')

def mark_point(plot, fn, x):
    plot.scatter(x, eval_math_fn(fn, {'x': x}), marker='o', c='red')