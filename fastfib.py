def fib(length):
	first, second = 1, 1
	if length < 2:
		return length
	else:
		length -= 2
		for i in range(length):
			second, first = first+second, second
