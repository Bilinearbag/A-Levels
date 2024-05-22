#STACK (LAST IN FIRST OUT - First item added is the last item removed from stack)
def push(array,tp):
    if tp==(len(array)-1):
        print("Stack is full.")
    else:
        val=int(input("Enter a value: "))
        tp=tp+1
        array[tp]=val
    return array,tp

def pop(array,tp,rp):
    if tp==rp:
        print("Stack is empty")
    else:
        array[tp]=""
        tp=tp-1
    return array,tp


#QUEUE (FRIST IN FIRST OUT - First item added is the first item removed from the queue)
def enqueue(array,fp,ep):
    if ep==(len(array)-1):
        print("Queue is full.")
    else:
        val=int(input("Enter a value: "))
        ep=ep+1
        array[ep]=val
    return array,fp
    
def dequeue(array,fp,ep):
    if len(array)==0:
        print("queue is empty.")
    else:
        fp=fp+1
    return array,fp


def circenqueue(): #CIRCULAR QUEUE
    global Data, front, end, NumElements
    val=int(input("Enter a value: "))
    if NumElements==len(Data):
        print("Queue is full")
    else:
        Data[end] = val
        if end == len(Data)-1:
            end = 0
        else:
            end+=1
        NumElements+=1

def circdequeue(): #CIRCULAR QUEUE 
    global Data, front, end, NumElements
    if NumElements==0:
        print("Queue is empty")
    else:
        if front == len(Data)-1:
            front = 0
        else:
            front+=1
        NumElements-=1


#Main Program
Data=[1,3,5,7]
top=3
rear=0
front=0
end=3
Size = 4
NumElements = 4
