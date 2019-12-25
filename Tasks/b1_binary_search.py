from typing import Any, Sequence, Optional

g = [i for i in range(1, 100)]
def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	min = 0
	max = len(arr) - 1
	while min + 1 < max:
		mid = (min + max) // 2
		if arr[mid] > elem:
			max = mid
		if arr[mid] < elem:
			min = mid
		if arr[mid] == elem:
			return mid
	if arr[min] == elem:
		return min
	elif arr[max] == elem:
		return max
	else:
		return None

if __name__ == '__main__':
	print(binary_search(31, g))