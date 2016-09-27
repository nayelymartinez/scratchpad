# mid-August 2016
# Algorithm Whiteboarding
# Recurse Center
# About: Validates whether opening and closing tags '(', '[', '{' match up using a stack. Part of someone else's interview question.

class Stack:
	def __init__(self):
		self.array = []

	def push(self, char):
		self.array[len(self.array) - 1] = char

	def pop(self):
		char = self.array[len(self.array) - 1]
		return char

	def peek(self):
		if self.size() == 0:
			return None
		else:
			char = self.array[len(self.array) - 1]
			return char

	def size(self):
		return len(self.array)

def validate(str):
	stack = Stack()
	for char in str:
		response = check(char)
		if response:
			stack.push()

def check(char):
	# Case 1: List is empty
	if char == '}' or char == ')' or char = ']':
		if stack.peek() is None:
			return False
	# Case 2: Incoming closing char does not match top of stri
	if char == '}' and stack.peek() != '{':
		return False
	elif char == ']' and stack.peek() != '[':
		return False
	elif char == ')' and stack.peek() != '(':
		return False

	# Case: Incoming string is closing parentheses
		# If empty stack -> BAD OR peek() is not corresponding opening tag -> BAD
	# Case: Incoming string is opening parentheses:
		# Pass


def main():
	response = validate("def ()")

if __name__ == '__main__':
	main()

# MINE:
# Comments: GOOD: Started out with some examples
# Comments: DELTA: took a bit to get started, could tell you were sort of mulling the problem over and kind of poking it from different sides which is good
# Comments: GOOD: I think I just realized a problem with this
# Comments: "In the 5 minutes left, let's take note of that. The correction we need is to use this other data structure, maybe a dictionary"

# HIS:
#Comments: clear thought process
# Critique was that I am a little rusty
# Weakness was that I got caught in control structure and did not commit to 

# OTHERS
# Comments: stayed game and articulate
# Comments: when I'm a woman programmer, almost hyper-sensitive when it comes to people patronizing
# Examples: if someone says, yes, I understand what you're saying.
# Part of the interview is your programming skills, but also what it would be like to work with you 

# Set up examples on the RHS side and leave everything else on the LHS
