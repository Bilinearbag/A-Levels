#BINARY TREE
def Addnode():
    global ArrayNodes
    global RootPointer
    global FreeNode

    NodeData = int(input("Enter the Data:"))

    #Check if there is space in the array or not
    if FreeNode <= 19:
        #First Create a node and initialize
        ArrayNodes[FreeNode][0] = -1 #left pointer of freenode
        ArrayNodes[FreeNode][1] = NodeData #data of freenode
        ArrayNodes[FreeNode][2] = -1 #right pointer of freenode

        #First check if you have a root value means is it empty
        if RootPointer == -1:
            RootPointer =0
        else:
            placed = False
            currentpointer = RootPointer
            #find the correct position and adjust the pointers (LEFT RIGHT)
            while placed == False:
                #if it is smaller so left
                if NodeData< ArrayNodes[currentpointer][1]:
                    #need to check first if it is empty or not
                    #if it is empty (-1) then just store else increment
                    if ArrayNodes[currentpointer][0] == -1:
                        ArrayNodes[currentpointer][0] = FreeNode
                        placed = True
                    else:
                        currentpointer=ArrayNodes[currentpointer][0]
                
                else:
                    #this is else if value is > root so move towards right or check if it is empty
                    if ArrayNodes[currentpointer][2] == -1:
                        ArrayNodes[currentpointer][2] = FreeNode
                        placed = True
                    else:
                        #increment right
                        currentpointer = ArrayNodes[currentpointer][2]
        
        FreeNode += 1
    else:
        print("this tree is full")

def Findnode(searchval):
    global RootPointer
    global ArrayNodes

    currentpointer = RootPointer

    #while loop for searching
    while currentpointer != -1 and ArrayNodes[currentpointer][1] != searchval:
        if searchval < ArrayNodes[currentpointer][1]:
            currentpointer = ArrayNodes[currentpointer][0]
        else:
            currentpointer = ArrayNodes[currentpointer][2]
    print(currentpointer)

#TRAVERSAL

#IN ORDER (LEFT, ROOT, RIGHT)
def inorder(root):
    global BinaryTree

    if BinaryTree[root][0] != -1: #if there is value at the left pointer of the root
        inorder(BinaryTree[root][0]) #recursion; take left pointer as root and check again
    print(BinaryTree[root][1])
    if BinaryTree[root][2] != -1: #if there is value at right pointer of the root
        inorder(BinaryTree[root][2]) 

#POST ORDER (LEFT RIGHT ROOT)
def postorder(root):
    global BinaryTree

    if BinaryTree[root][0] != -1: #first checks left pointer
        postorder(BinaryTree[root][0]) #performs traversal for left 
    if BinaryTree[root][2] != -1: #after traversal done left, unwinds and goes to right
        postorder(BinaryTree[root][2])
    print(BinaryTree[root][1]) 

def preorder(root):
    global BinaryTree

    print(BinaryTree[root][1])
    if BinaryTree[root][0] != -1:
        preorder(BinaryTree[root][0])
    if BinaryTree[root][2] != -1:
        preorder(BinaryTree[root][2])


#Main program for adding and finding nodes
"""
ArrayNodes = [[0] * 3 for x in range(20)]
RootPointer = -1
FreeNode = 0
print("Rootpointer:", RootPointer)
print("Free Node:", FreeNode)
for x in range(20):
    print(ArrayNodes[x])

Findnode(30)
"""

#Main program for Traversal:
FreeNode = 6
RootPointer = 0
BinaryTree = [[1, 20, 5], [2, 15, -1], [-1, 3, 3], [-1, 9, 4], [-1, 10, -1], [-1, 58, -1], [-1, -1, -1]]

preorder(RootPointer)


