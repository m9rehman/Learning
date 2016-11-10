def mergesort(array):
	results= []
	n = len(array)
	if n < 2:
		return array
	else:
		middle = int(len(array)/2)
		leftSorted = mergesort(array[:middle])
		rightSorted = mergesort(array[middle:])
		return merge(leftSorted,rightSorted,n)



def merge(l,r,n):
	results = []
	i=0
	j=0
	while i < len(l) and j < len(r):
		if l[i] < r[j]:
			results.append(l[i])
			i+=1 
		else:
			results.append(r[j])
			j+=1
	#Copying in any other results
	results += l[i:]
	results += r[j:]
	return results

