import re
def check_brackets(brackets_row: str) -> bool:
	"""
	Check whether input string is a valid bracket sequence
	Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
	:param brackets_row: input string to be checked
	:return: True if valid, False otherwise
	"""
	some_row = brackets_row
	x = r"^\)"
	if re.match(x, some_row):
		return False
	else:
		l_bracket = r"\("
		r_bracket = r"\)"
		l_res = len(re.findall(l_bracket, some_row))
		r_res = len(re.findall(r_bracket, some_row))
		if l_res == r_res:
			return True
		else:
			return False
