def insertionsort():
    global Data
    arraysize = len(Data)
    for pointer in range(1,arraysize):
        valtoinsert = Data[pointer]
        position = pointer

        while (position>0) and (Data[position-1]>valtoinsert):
            Data[position] = Data[position-1]
            position -= 1
        Data[position] = valtoinsert


def bubblesort():
    global Data
    temp=0
    for x in range(len(Data)):
        for i in range((len(Data))-1):
            if Data[i]>Data[i+1]:
                temp=Data[i+1]
                Data[i+1]=Data[i]
                Data[i]=temp
    return Data

#Main Program
Data=[1,3,5,7]
