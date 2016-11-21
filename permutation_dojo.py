from math import factorial

def main():
	num = 999999
	fact_lst = []
	while num > 0:
		for i in range(2, 11):
			if factorial(i) >= num:
				fact_num = factorial(i - 1)
				loop_num = int(num/fact_num)
				if loop_num != 0:
					fact_lst.append((i - 1,loop_num))
				num -= fact_num * loop_num
				continue
	print(fact_lst)
	loop_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
	result = []
	for i in range(len(fact_lst)):
		result_num = list(loop_set)[fact_lst[i][1]]
		loop_set.remove(result_num)
		print(result_num)
	print(list(loop_set)[0])

main() 

