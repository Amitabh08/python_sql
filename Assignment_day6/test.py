from Assignment1 import LinkedList
def main():
    LL = LinkedList()

    for i in range(100,1000,100):
        LL.append(i)
    
    print("LINKED LIST : ",end = " ")

    LL.info()

    LL.get_value(2)
    print("insertion operations: ", end= " ")
    LL.append(1000)
    LL.insertAtbegin(50)
    LL.insertAtposition(550,6)
    LL.info()

    print("REMOVING ELEMENTS FROM THE LINKED LIST: ", end = " ")
    LL.remove_at_index(5)
    LL.remove_at_index(0)
    LL.info()
    print(LL.count(100))
    print(100 in LL)

    # print("DELETING ALL ELEMENTS: ", end = " ")
    # LL.clear()
    # LL.info()


if(__name__=='__main__'):
    main()