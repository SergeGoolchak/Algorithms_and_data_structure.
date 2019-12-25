import re
from Tasks.a0_my_stack import some_list
import Tasks.a0_my_stack as m


def check_brackets(brackets_row: str) -> bool:
	"""
	Check whether input string is a valid bracket sequence
	Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
	:param brackets_row: input string to be checked
	:return: True if valid, False otherwise
	"""
	m.clear()
	for i in brackets_row:
		global some_list
		if i == "(":
			m.push(i)
		if i == ")":
			if len(some_list) > 0:
				m.pop()
			else:
				return False
		print(some_list)
	return len(some_list) == 0



if __name__ == '__main__':
	print(check_brackets("(()))"))

