class Node():
    def __init__(self,data):
        self.data =data
        self.next = None
    
class singlyLinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
    def insertAtEnd(self,data):
        newNode = Node(data)
        if(self.tail is None):
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode 
            self.tail = newNode
    def printLinkedList(self):
        temp = self.head
        while(temp is not None):
            print(temp.data , end =' ')
            temp = temp.next 

def main():
    print("running")
    sll = singlyLinkedList()
    arr = [1,4,2,5]#list(map(int,input().split()))
    for i in range(len(arr)):
        sll.insertAtEnd(arr[i])
    sll.printLinkedList()

if __name__ == "__main__":
    main()

