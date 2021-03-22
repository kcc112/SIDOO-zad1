from scipy import optimize
from utils.eval_math_fn import eval_math_fn


def scipy_optimize(fun, interval_start, interval_end, epsilon, iter_count):
    def f(x):
        return eval_math_fn(fun, {'x': x})

    result = optimize.minimize_scalar(f, bounds=(interval_start, interval_end), method='bounded', options={'maxiter': iter_count, 'xatol': epsilon})
    minimum = result.x
    print(f'Minimum wg. scipy: {minimum}')
    return minimum;
