




def quick_sort(arr, left, right):
	index  = partition(arr, left, right)
	if left < index - 1:
		quick_sort(arr, left, index-1)
	if index < right:
		quick_sort(arr, index, right)
	return arr



def partition(arr, left, right):
	pivot = arr[(left + right) // 2]
	while  left <= right:
		while arr[left] < pivot:
			left += 1
		while arr[right] > pivot:
			right -= 1
		if left <= right:
			arr[left], arr[right] = arr[right], arr[left]
			left += 1
			right -= 1
	return left




a = [6,5,4,3,2,1]
print(quick_sort(a, 0, 5))

