# Merge Sort implementation
# Author: Nayely Martinez
# Date: 10/22/16 
# Description: Recursive merge sort implementation in Python

def merge_sort(lst):
	if len(lst) <= 1:
		return lst
	else:
		p = 0
		r = len(lst)
		q = (r-p)//2
		left_lst = lst[p:q]
		right_lst = lst[q:r]
		left_sorted = merge_sort(left_lst)
		right_sorted = merge_sort(right_lst)
		merged = merge(left_sorted, right_sorted)
		return merged

def merge(lst1, lst2):
	t1 = 0
	t2 = 0
	merged = []
	while t1 < len(lst1) and t2 < len(lst2):
		if lst1[t1] <= lst2[t2]:
			merged.append(lst1[t1])
			t1 += 1
			if t1 == len(lst1) and t2 <= len(lst2):
				merged.extend(lst2[t2:])
				break
		else:
			merged.append(lst2[t2])
			t2 += 1
			if t2 == len(lst2) and t1 <= len(lst1):
				merged.extend(lst1[t1:])
				break
	return merged

def test():
	lsts = [
		[],
		[4],
		[9,2],
		[8, 2, 11, 7, 1, 5, 6, 4]
	]
	for l in lsts:
		print("\nInput (unsorted):", l)
		print("Output (sorted):",merge_sort(l))

	assert merge_sort(lsts[0]) == [], "Did not sort correctly"
	assert merge_sort(lsts[1]) == [4], "Did not sort correctly"
	assert merge_sort(lsts[2]) == [2,9], "Did not sort correctly"
	assert merge_sort(lsts[3]) == [1,2,4,5,6,7,8,11], "Did not sort correctly"

def main():
	test()
	return


if __name__ == '__main__':
	main()