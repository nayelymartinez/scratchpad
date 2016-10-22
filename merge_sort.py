import math

def merge_sort(merged, lst, p, r):
	if len(lst) <= 1:
		print("Less or equal to 1", lst)
		return lst
	else:	
		q = len(lst)//2
		l_lst = lst[p:q]
		r_lst = lst[q:r]
		print("L:",l_lst)
		print("R:",r_lst)
		print("p:", p)
		print("q:", q)
		print("r:", r, "\n")
		left_to_sort = merge_sort(merged, l_lst, 0, len(l_lst))
		right_to_sort = merge_sort(merged, r_lst, 0, len(r_lst))
		print("\n ** Ready to merge **")
		print("Left to merge:", left_to_sort)
		print("Right to merge:", right_to_sort)
		merged = merge(merged, left_to_sort, right_to_sort)
		print("Merged so far:",merged, "\n")
		return merged

def merge(merged_lst, lst1, lst2):
	t1 = 0
	t2 = 0
	print("Lst1 to merge:", lst1)
	print("Lst2 to merge:", lst2)
	while t1 <= len(lst1) and t2 <= len(lst2):
		if lst1[t1] <= lst2[t2]:
			merged_lst.append(lst1[t1])
			t1 += 1
			# Add remaining list2 items (if any) if reached end of list1
			if t1 >= len(lst1):
				merged_lst.extend(lst2[t2:])
				return merged_lst
		else:
			merged_lst.append(lst2[t2])
			t2 += 1
			if t2 >= len(lst2):
				merged_lst.extend(lst1[t1:])
				return merged_lst

def merge_it(merged_lst,lst1, lst2):
	t1 = 0
	t2 = 0
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
		#[8, 2, 11, 7, 1, 5, 6, 4],
		#[], 
		#[4],
		[1, 5, 2, 4]
	]
	print("Final merged list:",merge_sort([],int_lst[0], 0, len(int_lst[0])-1))

if __name__ == '__main__':
	main()
