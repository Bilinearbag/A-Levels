#Linear Searching:
def linearsearch(val,array):
    for x in range(len(array)):
            if array[x]==val:
                print(x)



#Binary Searching:
def binarysearch(val,array):
    lower=0
    upper=(len(array))-1
    Found=False
    notinlist = False
    while (Found==False) and (notinlist==False):
        Mid=int((lower+upper)/2)
        if val==array[Mid]:
            print(Mid)
            Found=True
        else:
            if array[Mid]<val:
                lower = Mid +1
            else:
                upper=Mid-1

        if lower>upper:
            notinlist=True
    if Found == True:
        print("val found")
    else:
        print("val not in list")


#Main Prgoram
Data=[1,3,5,7]
