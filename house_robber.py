# Dynamic Programming: House Robber
# Date: October 31, 2016
# Author: Nayely Martinez (nayely.e.martinez@gmail.com)
# Description: Recursive solution to house robber problem. 
# Given a list of values for a neighborhood of "houses", return the maximum value if no two adjacent houses (values) in the list can be robbed. 

def robber(house_lst):
	if len(house_lst) == 1:
		return house_lst[0]

def main():
	house_lst = [4]
	print(robber(house_lst))

main()