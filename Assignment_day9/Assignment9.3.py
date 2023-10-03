#FIND EVENS AND PRIMES IN A LINKEDLIST

class node:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node
    

    def size(self):
        length = 1
        current_node = self.head
        if self.head is None:
            print("Empty list ")
        else:
            while (current_node.next):
                length += 1
                current_node = current_node.next
            print(length)

    def info(self):
            self.print_linkedlist()
            print("SIZE OF LINKED LIST IS: ", end = " ")
            self.size()

    def print_linkedlist(self):
        current_node = self.head
        while(current_node):
            print(current_node.data, end =" ")
            current_node = current_node.next
        print()

    def isEven(self):
        current_node = self.head
        while(current_node):
            if current_node.data % 2 == 0:
                print(current_node.data, end =" ")
            current_node = current_node.next
        print()

    def isPrime(self,value):
        if value > 1:
            for i in range(2,value):
                if(value % i == 0):
                    return False
        
            return True
        
    def findPrimes(self):
        current_node = self.head
        while (current_node):
            if self.isPrime(current_node.data):
                print(current_node.data, end = " ")
            current_node = current_node.next


LL = LinkedList()

if __name__ == '__main__':

    for i in range(10,20):
        LL.append(i)

    print("LINKED LIST : ",end = " ")
    LL.print_linkedlist()
    LL.isEven()
    LL.findPrimes()
