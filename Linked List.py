#LINKED LIST

#CREATE LINKED LIST
class node:
    def __init__(self, DataP, nextNodeP):
        self.Data = DataP   #PUBLIC Data : INTEGER
        self.nextNode = nextNodeP   #PUBLIC Data : INTEGER



#PRINT LINKED LIST:
def printlinklist():
    global linkedlist
    global startpointer
    currentpointer = startpointer
    while currentpointer != -1:
        print(linkedlist[currentpointer].Data)
        currentpointer = linkedlist[currentpointer].nextNode



#SEARCHING LINKED LIST
def finditem(currentpointer, searchval):
    global linkedlist
    while currentpointer!= -1:
        if linkedlist[currentpointer].Data == searchval:
            return currentpointer
        else:
            currentpointer=linkedlist[currentpointer].nextNode
    return currentpointer



#UNORDERED LINKED LIST INSERTION
def unorderedInsertion(currentpointer):
    global linkedlist
    global emptylist

    data = int(input("Enter a value to append:"))
    if emptylist<0 or emptylist>9:
        return False #Linked List is full
    else: #INCREMENT EMPTYLIST POINTER AFTER STORING IT IN TEMPORARY VARIABLE 
        freelist = emptylist
        emptylist = linkedlist[emptylist].nextNode

        #CREATE NEW NODE
        newNode = node(data, -1)
        
        #STORE NEW NODE WHERE FREELIST IS POINTING TO 
        linkedlist[freelist] = newNode

        #FIND THE LAST NODE INDEX
        previouspointer = 0
        while currentpointer != -1:
            previouspointer = currentpointer
            currentpointer = linkedlist[currentpointer].nextNode
        linkedlist[previouspointer].nextNode = freelist
        return True



#ORDERED LINKED LIST INSERTION
def orderedInsertion(currentpointer):
    global linkedlist
    global emptylist
    global startpointer

    data = int(input("Enter a value to add:"))
    if emptylist<0 or emptylist>9:
        return False #Linked list is full
    else: #INCREMENT EMPTYLIST POINTER AFTER STORING IT IN TEMPORARY VARIABLE
        freelist = emptylist
        emptylist = linkedlist[emptylist].nextNode
        
        #CREATE NEW NODE
        newNode = node(data, -1)

        #STORE NEW NODE WHERE FREELIST IS POINTING TO 
        linkedlist[freelist] = newNode
        
        previouspointer = 0
        while currentpointer!=-1 and linkedlist[currentpointer].Data<data: #FIND POSITION WHERE VAL NEEDS TO BE STORED
            previouspointer = currentpointer 
            currentpointer = linkedlist[currentpointer].nextNode
        if currentpointer == startpointer:
            linkedlist[freelist].nextNode = startpointer
            startpointer = freelist
        else:
            linkedlist[freelist].nextNode = linkedlist[previouspointer].nextNode
            linkedlist[previouspointer].nextNode = freelist 

        return True

#DELETING A NODE 

def deletenode(currentpointer):
    global startpointer
    global linkedlist
    global emptylist
    delval = int(input("Enter value to delete:"))
    if emptylist<0 or emptylist>9:
        return False #Linked list is empty
    else:
        previouspointer = 0 #Search the index of the element you want to remove
        while currentpointer!=-1 and linkedlist[currentpointer].Data != delval:
            previouspointer = currentpointer
            currentpointer = linkedlist[currentpointer].nextNode
        
        #First condition check if val to be deleted exists or not:
        if currentpointer == -1:
            return False #does not exist
        else: 
            #Does exist; In this case we will have two cases:
            
            #Case 1: If value to be deleted is the first value
            if currentpointer == startpointer:
                startpointer = linkedlist[startpointer].nextNode
            
            else: #Case 2: if Value to be deleted is in between
                linkedlist[previouspointer].nextNode = linkedlist[currentpointer].nextNode
            
            #Add deleted node to empty list
            linkedlist[currentpointer].Data = 0
            linkedlist[currentpointer].nextNode = emptylist
            emptylist = currentpointer
            
            return True
            
        

        
#Main Program
linkedlist = [node(1,1), node(5,4), node(6,7), node(7,-1), node(2,2), node(0,6), node(0,8), node(56,3), node(0,9), node(0,-1)]
startpointer = 0
emptylist = 5

printlinklist()
