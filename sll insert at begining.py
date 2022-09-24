class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

class singlyLinkedList():
    def __init__(self):
        self.head = None 
    
    def insertAtBeggining(self,data):
        newNode = Node(data)
        if(self.head is None):
            self.head = newNode
        else:
            newNode.next = self.head 
            self.head = newNode 
        
    def printLinkedList(self):
        temp = self.head 
        while(temp is not None):
            print(temp.data , end = ' ')
            temp = temp.next 

def main():
    sll = singlyLinkedList()
    arr = [5,1,2,4,3]#list(map(int,input().split()))
    for i in range(len(arr)):
        sll.insertAtBeggining(arr[i])
    sll.printLinkedList()

if __name__ == "__main__":
    main()
    
