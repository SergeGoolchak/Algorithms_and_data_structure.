"""
My little Stack
"""
from typing import Any

some_list = []
def push(elem: Any) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	global some_list
	some_list.insert(0, elem)
	print(elem)
	return None



def pop() -> Any:
	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	global some_list
	if not some_list:
		return None
	else:
		r = some_list[0]
		del some_list[0]
		return r


def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	global some_list
	return some_list[ind]


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	global some_list
	some_list.clear()
	return None

if __name__=='__main__':
	push(9)
	push(2)
	push(99)
	push(14)
	print(some_list)
	print(pop())
	print(some_list)
	print(peek(2))
	clear()
	print(some_list)


