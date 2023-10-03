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

    def insertAtbegin(self, data):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node
        


    def insertAtposition(self,data,index):
        new_node = node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        position = 0
        if position == index:
            self.insertAtbegin(data)
        else:
            while position + 1 != index and current_node != None:
                position+=1
                current_node = current_node.next
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                return f'INDEX NOT PRESENT IN THE LINKED LIST'
            
    def get_value(self,index):
        current_node = self.head
        position = 0
        if self.head is None:
            return f' LINKED LIST EMPTY '
        while position + 1 != index and current_node != None:
            position += 1
            current_node = current_node.next
            get_node_value = current_node.next.data
        print(f'FETCHED DATA IS: {get_node_value}')
        return get_node_value

    def set_value(self, value, index):
        current_node = self.head
        position = 0
        if self.head is None:
            return f' LINKED LIST EMPTY '
        while position + 1 != index and current_node != None:
            position += 1
            current_node = current_node.next
        current_node.next.data = value


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

    def remove_first_node(self):
        if(self.head == None):
            return
 
        self.head = self.head.next
 
    def remove_last_node(self):
 
        if self.head is None:
            return
 
        current_node = self.head
        while(current_node.next.next):
            current_node = current_node.next
 
        current_node.next = None
 
    def remove_at_index(self, index):
        if self.head == None:
            return
 
        current_node = self.head
        position = 0
        if position == index:
            self.remove_first_node()
        else:
            while(current_node != None and position+1 != index):
                position = position+1
                current_node = current_node.next
 
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index not present")

    def clear(self):
        self.head = None
        print("DELETED")
        
    def print_linkedlist(self):
        current_node = self.head
        while(current_node):
            print(current_node.data, end =" ")
            current_node = current_node.next
        print()

    def findPrimes(self,n):
        if n <= 1:
            return False
        if n <=3:
            return True
        
        if (n % 2 == 0 or n % 3 == 0) :
            return False
 
        i = 5
        while ( i * i <= n) :
            if (n % i == 0 or n % (i + 2) == 0) :
                return False
            i = i + 6
        return True
    

    def count(self, data):
        temp = self.head
        count = 0
        while temp != None:
            if(temp.data == data):
                count += 1
            temp = temp.next
        return count

    def __str__(self):
        output = '('
        temp = self.head
        while temp != None:
            output += str(temp.data) + ','
            temp = temp.next
        output +=')'
        return output 

    def __contains__(self, data):
        temp = self.head
        while temp != None:
            if temp.data == data:
                return True
            temp = temp.next
        return False







    

    





    



