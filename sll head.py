class Node():
    def __init__(self,data):
        self.data = data
        self.next = None 
    
class singlyLinkedList():
    def __init__(self):
        self.head = None
    def insertAtEnd(self,data):
        newNode = Node(data)
        if(self.head is None):
            self.head = newNode
            print(self.head.data)
            print("the first head is", self.head)
        else:
            temp = self.head
            print("out",temp.data)
            while(temp.next is not None):
                print("WHILE NOT NONE")
                temp = temp.next
                print("data = ",temp.data)
                print("the temp is",temp)
                print("upcoming")
                
            temp.next = newNode
            print("next is",temp.next,'  ',temp.data)

    def printLinkedList(self):
        temp = self.head
        while(temp is not None):
            print('',temp,' ',temp.data, ' ' , temp.next)
            temp = temp.next

def main():
    sll = singlyLinkedList()
    arr = [1,2,3,4,5,6]#list(map(int,input().split()))
    for i in range(len(arr)):
        sll.insertAtEnd(arr[i])
    sll.printLinkedList()

if __name__ == "__main__":
    main()    
