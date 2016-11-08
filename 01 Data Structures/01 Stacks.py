#Stack implementation using array
#	Each of these takes O(1) time since we are using arrays
def isStackEmpty(Stack):
	if Stack.top is None:
		return True
	else:
		return False

def pushStack(Stack,elem):
	Stack.top += 1
	Stack[Stack.top] = elem

def popStack(Stack):
	if isStackEmpty(Stack):
		print("Error: underflow")
		return
	else:
		return Stack[Stack.top]
		Stack.top -= 1

