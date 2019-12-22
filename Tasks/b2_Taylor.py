"""
Taylor series
"""
from typing import Union
from Tasks.c1_fact import factorial_iterative
import math


def ex(x: Union[int, float]) -> float:
	"""
	Calculate value of e^x with Taylor series

	:param x: x value
	:return: e^x value
	"""
	if x == 0:
		return 1
	counter = 0
	res = 1
	while counter < 50:
		counter += 1
		e = (x ** counter) / factorial_iterative(counter)
		res += e
	return res



def sinx(x: Union[int, float]) -> float:
	"""
	Calculate sin(x) with Taylor series

	:param x: x value
	:return: sin(x) value
	"""
	if x == 0:
		return 1
	counter = 0
	res = x
	while counter < 50:
		counter += 1
		if not counter % 2:
			e = (x ** (2 * counter + 1)) / factorial_iterative(2 * counter + 1)
			res += e
		if counter % 2:
			e = (x ** (2 * counter + 1)) / factorial_iterative(2 * counter + 1)
			res -= e
	return res

