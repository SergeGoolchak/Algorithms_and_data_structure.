from typing import Any, Sequence, Optional

s = [i for i in range(100)] + [101]
print(s)
print(s[-1])
def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	"""
	Performs binary search of given element inside of array (using recursive way)

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	d = 0
	w = -1
	if arr[len(arr) - 1] == elem:
		return len(arr) - 1
	if arr[d] == elem:
		return d
	mid = len(arr) // 2
	if arr[mid] == elem:
		return mid
	if elem not in arr:
		return None
	else:
		if arr[mid] > elem:
			return binary_search(elem, arr[:mid])
		if arr[mid] < elem:
			return binary_search(elem, arr[mid:])


print(binary_search(5,s))