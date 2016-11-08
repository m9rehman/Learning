#Queues:
# Enqueue, Dequeue, Empty
# Have 2 pointers/indices to track: Write index (Where to write next) and Read Index (Where to read next) 

#Queue (size: n-1) implemented using array of size (n)

# Empty is enqueue and dequeue indices are the same. Buffer of one element so no confusion is Queue is full/empty
# Implemented using indices that cycle through queue
def isQueueEmpty(Queue):
	if Queue.indexE == Queue.indexD:
		return True
	else:
		return False

def Enqueue(Queue, elem):
	if isQueueEmpty(Queue):
		Queue[indexE] = elem
		Queue.indexE++
	elif Queue.indexE == Queue.indexD - 1:
		print("Error: Queue full")
		return
	else:
		Queue[indexE] = elem
		(indexE++) % len(Queue)  