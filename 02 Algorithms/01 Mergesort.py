def mergesort(array):
	if len(array)> 1:
		middle = len(array)/2
		leftArray = array[:middle]
		rightArray = array[middle:]

		leftSorted = mergesort(leftArray)
		rightSorted = mergesort(rightArray)
		return merge(leftSorted, rightSorted, len(array))


def merge(lSorted,rSorted,n):
	li,ri=0
	sortedArray = []
	for i in range(0,n):
		if (lSorted[li] <= rSorted[ri]):
			sortedArray[i] = lSorted[li]
			li += 1
		else:
			sortedArray[i] = rSorted[ri]
			ri += 1
	return sortedArray
