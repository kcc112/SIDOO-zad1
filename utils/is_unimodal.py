# http://optymalizacja.w8.pl/PrzedzialyUnimodalnosci.html
from utils.eval_math_fn import eval_math_fn


def is_unimodal(interval_start, interval_end, fn, step):
	x = (interval_start + interval_end) / 2

	if (eval_math_fn(fn, {'x': interval_start}) > eval_math_fn(fn, {'x': x})) and (eval_math_fn(fn, {'x': interval_end}) > eval_math_fn(fn, {'x': x})):
		print(
			f'Funkcja jest prawdopodobnie unimodalna w przedziale [{interval_start}, {interval_end}]')
		return True
	else:
		new_interval_start = x - step
		new_interval_end = x + step
		counter = 0

		print(
			f'Funkcja nie jest unimodalna w przedziale [{interval_start}, {interval_end}]')

		while not (eval_math_fn(fn, {'x': new_interval_start}) > eval_math_fn(fn, {'x': x})) and (eval_math_fn(fn, {'x': new_interval_end}) > eval_math_fn(fn, {'x': x})) and counter <= 100:
			new_interval_start -= step
			new_interval_end += step
			counter += 1

			
		if counter <= 100:
			print(
				f'Funkcja jest unimodalna w przedziale [{new_interval_start}, {new_interval_end}]')
		else:
			print(
				f'Funkcja prawdopodobnie nie posiada minimum lokalnego')

		return False
