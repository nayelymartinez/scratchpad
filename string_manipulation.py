# Date: September 9, 2016
# String Manipulation Practice in Python
# Remember: In Python, a string is just a LIST of characters in some order.
# 	All list methods are fair game when doing work on strings.

 
 #Given an input string and ordering string, need to return true
 #if the ordering string is present in the input string.
 #'''

 # INCORRECT because there are some edge cases where this wouldn't be the case
 # Incorrect ex. input = "hello worldo!", ordering: "hlo!"
 # Runtime: O(n^2)
 # Start at the end of the input. 
 # Traverse backwards until you find the first (really the last) instance of
 # ordering string. Add index to array of len(ordering_string). 
 # if no index found, return False (missing char)
 # elif recurse through array. if number is less than any num currently in array,
 	# return false
 # else add index to array
 # if reached end of ordering string, return True

# 2nd Strategy:
# Keep track of index min and max for each char in ordering. 
# After traversing array for min and max of current char:
# If the next char's min is less than last char's max, return False

def check_string_order(input_str, ord_str):
	last_min = len(ord_str)
	last_max = 0
	for i in range(len(ord_str)):
		# Update min and max
		str_min = input_str.find(ord_str[i])
		str_max = input_str.rfind(ord_str[i])
		# Check rule still apply
		if str_min != -1:
			if str_min < last_max:
				return False
		else:
			return False
	return True

def main():
	input_str = "hello world!"
	ordering_str = ""
	print(check_string_order(input_str, ordering_str))

if __name__ == '__main__':
	main()
