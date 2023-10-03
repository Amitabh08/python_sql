class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def swapNodes(self, x, y):

		if x == y:
			return

		previousX = None
		currrentX = self.head
		while currrentX != None and currrentX.data != x:
			previousX = currrentX
			currrentX = currrentX.next

		prevY = None
		currrentY = self.head
		while currrentY != None and currrentY.data != y:
			prevY = currrentY
			currrentY = currrentY.next

		if currrentY == None or currrentY == None:
			return

		if previousX != None:
			previousX.next = currrentY
		else: 
			self.head = currrentY

		if prevY != None:
			prevY.next = currrentX
		else: 
			self.head = currrentX

		temp = currrentX.next
		currrentX.next = currrentY.next
		currrentY.next = temp

	def bubbleSort(self):
		count = 0
		start = self.head
		while start != None:
			count += 1
			start = start.next

		for i in range(0, count):

			start = self.head
			while start != None:

				ptr = start.next
				if ptr != None:
					if start.data > ptr.data:
						self.swapNodes(start.data, ptr.data)

				start = start.next

	def printList(self):
		tmp = self.head
		while tmp != None:
			print(tmp.data, end=" ")
			tmp = tmp.next
		print("None")


if __name__ == '__main__':

	arr = [78, 20, 10, 32, 5,77,-8,1]

	llist = LinkedList()
	llist.head = Node(arr[0])
	start = llist.head
	for i in range(1, len(arr)):
		start.next = Node(arr[i])
		start = start.next

	print("Linked list before sorting")
	llist.printList()

	llist.bubbleSort()

	print("Linked list after sorting")
	llist.printList()

