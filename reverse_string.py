""" Coding Practice #1: String Manipulation """
# Date: August 6, 2016

# Recursive version
# Spacetime:
# Runtime: O(n)
def reverse(string):
	if len(string) == 0:
		return ""
	elif len(string) == 1:
		return string
	else:
		return string[len(string) - 1] + reverse(string[1:len(string) - 1]) + string[0]

def reverse_memo(string):
	if len(string) == 0:
		return ""
	elif len(string) == 1:
		new = string
		return string
	else:
		new = string[len]

# Using new variables
# Spacetime: O(n^2)
# Runtime: O(n)
def reverse2(string):
	new = ""
	for i in range(len(string)):
		new = new + string[len(string) - i - 1]
		print(new)

def main():
	new = reverse("Race car in the backseat.")
	print(new)
	#reverse2("Hello")
	return

if __name__ == '__main__':
	main()
