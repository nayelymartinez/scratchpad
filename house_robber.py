# Dynamic Programming: House Robber
# Date: October 31, 2016
# Author: Nayely Martinez (nayely.e.martinez@gmail.com)
# Description: Recursive solution to house robber problem. 
# Given a list of values for a neighborhood of "houses", return the maximum value if no two adjacent houses (values) in the list can be robbed. 

# [4]
# [4, 3]
# [3, 4]
# [3, 4, 5]
# [3, 4, 1]


def robber(house_lst, opt1 = 0, opt2 = 0):
	if len(house_lst) == 1:
		return house_lst[0]
	else:
		opt1 += house_lst[0]
		#print("Opt1:", opt1)
		opt2 += robber(house_lst[1:], opt2, opt1)
		#print("Opt2", opt2)
		maximum = max(opt1, opt2)
		return maximum


def main():
	house_lst = [3, 5, 1, 2]
	print(robber(house_lst, 0))

main()

# opt1 = 0 + 3
# opt2 = 0 + robber([4, 5, 1], 0, 3)
# 	=> opt1 = 0 + 4
# 		opt2 = 3 + robber([5, 1], 3, 4)
# 			=> opt1 = 3 + 5 = 8
# 				opt2 = 4 + robber([1], 4, 8)
# 					=> return 1
# 				maximum = max(8, 1)
# 				return 8
# 		maximum = max(4, 11)
# 		return 11