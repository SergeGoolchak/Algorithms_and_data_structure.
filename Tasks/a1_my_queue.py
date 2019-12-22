"""
My little Queue
"""
from typing import Any

queue = []
def enqueue(elem: Any) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	global queue
	queue.append(elem)
	return None


def dequeue() -> Any:
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	global queue
	if queue:
		r = queue[0]
		del queue[0]
		return r
	else:
		return None


def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	global queue
	if len(queue) >= ind:
		return queue[ind]
	else:
		return None


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	global queue
	queue.clear()
	return None

if __name__=='__main__':
