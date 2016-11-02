# Dynamic Programming: House Robber
# Date: October 31, 2016
# Author: Nayely Martinez (nayely.e.martinez@gmail.com)
# Description: Recursive solution to house robber problem. 
# Given a list of values for a neighborhood of "houses", return the maximum value if no two adjacent houses (values) in the list can be robbed. 

def robber(house_lst, maximum, opt1 = 0, opt2 = 0):
	if len(house_lst) == 1:
		return house_lst[0]
	else:
		opt1 += robber(house_lst[1:], maximum)
		opt2 += house_lst[0]
		#print(opt1, opt2)
		maximum += max(opt1, opt2)


def main():
	house_lst = [4, 5, 6]
	print(robber(house_lst))

main()