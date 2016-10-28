def main():
	string_arr = ["racecar", "racalr", "raccabr", "a", "bb"]
	for string in string_arr:
		print(string, is_palindrome(string))

def is_palindrome(string):
	left_pointer = 0
	right_pointer = len(string) - 1
	to_remove = -1
	while right_pointer >= left_pointer:
		if string[left_pointer] == string[right_pointer]:
			left_pointer += 1
			right_pointer -= 1
			continue
		# Not matching
		else:
			if string[left_pointer + 1] == string[right_pointer]:
				to_remove = left_pointer
				return to_remove
			elif string[right_pointer - 1] == string[left_pointer]:
				to_remove = right_pointer
				return to_remove
	return to_remove

	
if __name__ == "__main__":
	main()