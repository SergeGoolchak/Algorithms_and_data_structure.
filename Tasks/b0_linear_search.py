"""
This module implements some functions based on linear search algo
"""
from typing import Sequence

s = [99, 2, 1, 8, 101, 1]
def min_search(arr: Sequence) -> int:
	"""
	Function that find minimal element in array

	:param arr: Array containing numbers
	:return: index of first occurrence of minimal element in array
	"""
	r = 0
	for i in range(len(arr)):
		if arr[i] < arr[r]:
			r = i
	return r
