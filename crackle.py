def main():
	for i in range(1,101):
		if i%3 == 0:
			if i%5 == 0:
				print("CracklePop!")
			else:
				print("Crackle!")
		elif i%5 == 0:
			print("Pop!")
		else:
			print(i)
	return

if __name__ == '__main__':
	main()

	