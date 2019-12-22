def fib_recursive(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using recursive algorithm

	:param n: number of item
	:return: Fibonacci number
	"""
	if n < 0:
		raise ValueError
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fib_recursive(n - 1) + fib_recursive(n - 2)

def fib_iterative(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using iterative algorithm

	:param n: number of item
	:return: Fibonacci number
	"""
	if n < 0:
		raise ValueError
	numb1 = 0
	numb2 = 1
	counter = 1
	while counter < n:
		counter += 1
		numb1, numb2 = numb2, numb2 + numb1
	return numb2

