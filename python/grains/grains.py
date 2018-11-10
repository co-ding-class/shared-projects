def on_square(integer_number):
	if (integer_number) <= 0 or integer_number > 64:
		raise ValueError("that's not a square!")
	grain_number = 2 ** (integer_number - 1)
	return grain_number
	
def total_after(integer_number):
	if (integer_number) <= 0 or integer_number > 64:
		raise ValueError("that's not a square!")
	return 2 ** integer_number - 1

