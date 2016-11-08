#Stack implementation using array
#	Each of these stack operations takes O(1) time 
#	Stack.top is the top of the array

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

def topStack(Stack):
	if isStackEmpty(Stack):
		print("Error: underflow")
		return
	else:
		return Stack[Stack.top]


#TODO: Linked List implementation of stacks