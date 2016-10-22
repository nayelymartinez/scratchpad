import math

def merge_sort(lst, p, q, r):
	if len(lst) <= 2:
		return lst
	else:
		#q = int(math.floor((p-r))/2)
		l_lst = lst[p:q]
		r_lst = lst[q:r]
		print("L:",l_lst)
		print("R:",r_lst)
		return merge(merge_sort(l_lst, 0, int(math.floor(q-p)/2), q), merge_sort(r_lst, q, int(math.floor(r-q)/2), int(math.floor(len(lst)/2))))

def merge(lst1, lst2):
	t1 = 0
	t2 = 0
	merged_lst = []
	print("Lst1 to merge:", lst1)
	print("Lst2 to merge:", lst2)
	while (t1 < len(lst1)) and (t2 < len(lst2)):
		if lst1[t1] <= lst2[t2]:
			merged_lst.append(lst1[t1])
			print("Merged:",merged_lst)
			t1 += 1
			if t1 >= len(lst1):
				merged_lst.append(lst2[t2])
				print("Merged:",merged_lst)
				return merged_lst
		else:
			merged_lst.append(lst2[t2])
			print("Merged:",merged_lst)
			t2 += 1
			if t2 >= len(lst2):
				merged_lst.append(lst1[t1])
				print("Merged:",merged_lst)
				return merged_lst
		

def main():
	int_lst = [
		[8, 2, 11, 7, 1, 5, 6, 4],
		[], 
		[4],
		[1, 5, 2]
	]
	print(merge_sort(int_lst[0], 0, len(int_lst[0])//2, len(int_lst[0])))

if __name__ == '__main__':
	main()
