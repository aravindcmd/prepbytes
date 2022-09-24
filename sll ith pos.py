class Node():
    def __init__(self,data):
        self.data = data
        self.next = None 
    
class singlyLinkedList():
    def __init__(self):
        self.head = None 
        self.tail = None 
    
    def insertAtBeggining(self,data):
        newNode = Node(data)
        if(self.head is None):
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode 
    def insertAtEnd(self,data):
        newNode = Node(data)
        if(self.head is None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode 
            self.tail = newNode 
    def insertAtIthPos(self,data,i):
        if(i==0):
            self.insertAtBeggining(data)
        else:
            newNode = Node(data)
            count = 0
            temp = self.head
            while(temp.next is not None and count != i-1):
                temp = temp.next
                count +=1
            if(count == i-1):
                newNode.next = temp.next
                temp.next = newNode
            else:
                print("invalid input", i)
    def printLinkedList(self):
        temp = self.head 
        while(temp is not None):
            print(temp.data , end = ' ')
            temp = temp.next 
        print()

def main():
    sll = singlyLinkedList()
    arr = [5,4,3,2,1]
    for i in range(len(arr)):
        sll.insertAtEnd(arr[i])
    sll.printLinkedList()
    sll.insertAtIthPos(100,6)
    sll.printLinkedList()



if __name__ == "__main__":
    main()
    