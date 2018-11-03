def on_square(integer_number):
	if (integer_number) < 0:
		raise ValueError
	return 2 ** (integer_number - 1)
	
def total_after(integer_number):
	if (integer_number) < 0:
		raise ValueError
	return 2 ** integer_number - 1

