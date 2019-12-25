"""
Priority Queue

Queue priorities are from 0 to 5
"""
from typing import Any

queue = [[], [], [], [], [], []]

def enqueue(elem: Any, priority: int = 0) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	global queue
	queue[priority].append(elem)
	return None


def dequeue() -> Any:
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	global queue
	for i in range(len(queue)):
		while any(queue[i]):
			if not queue[i]:
				pass
			else:
				r = queue[i][0]
				del queue[i][0]
				return r



def peek(ind: int = 0, priority: int = 0) -> Any:
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	global queue
	if len(queue) >= priority:
		if len(queue[priority]) >= ind:
			return queue[priority][ind]
		else:
			return None
	else:
		return None


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	for i in range(len(queue)):
		queue[i].clear()
	return None


if __name__ == '__main__':
	enqueue(1, 0)
	enqueue(1, 1)
	enqueue(2, 1)
	print(queue)
	enqueue(4, 5)
	enqueue(8, 3)
	enqueue(5, 5)
	enqueue(99, 4)
	dequeue()
	print(queue)
	dequeue()
	dequeue()
	print(queue)
	print(peek(0, 7))
	clear()
	print(queue)

