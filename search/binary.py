 
def binarySearch (arr, l, r, x): 

	if r >= l: 

		mid = l + (r - l)/2

		if arr[mid] == x: 
			return mid 
		
		elif arr[mid] > x: 
			return binarySearch(arr, l, mid-1, x)  
		else: 
			return binarySearch(arr, mid + 1, r, x) 

	else: 
		return -1

arr = [ -2, 13, -4, 110, 40 ] 

print("is number 5 in list? :",binarySearch(5))
