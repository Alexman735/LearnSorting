def printspace(string):
    print(string)
    print("")

def bubbleSort(array, showme):
    # run loops two times: one for walking through the array 
    # and the other for comparison
    if(showme == True):
        printspace("Here is our original array: "+str(array)+". Let's Begin!")
    for i in range(len(array)):
        pointer = " ^  ^"
        stopindex = len(array) - i - 1
        if i != 0 and stopindex > 0 and showme == True:
            printspace("Now that everything up from element #"+str(stopindex)+" is in place, we no longer need to worry about that part. Now, we stop when we reach "+str(array[stopindex])+". We start again at 0!")
        if stopindex == 0 and showme == True:
            print("Done!")
            print("Final Result: ")
        arrayatprevj= 0  
        for j in range(0, stopindex):
            # To sort in descending order, change > to < in this line.
            amountofskip = "   "
            lookarr = [array[j], array[j+1]]
            if(j!=0):
                for x in lookarr:
                    integerdeterminer = 10
                    skipnumber = int(x / integerdeterminer)
                    while(skipnumber != 0 and x!=arrayatprevj):
                        amountofskip+=" "
                        integerdeterminer*=10
                        skipnumber = int(x / integerdeterminer)
                pointer = amountofskip+pointer
            if array[j] > array[j + 1]:
                
                # swap if greater is at the rear positio
                if(showme == True):
                    description = "BubbleSort sees that "+str(array[j])+" is greater than "+str(array[j+1])+" and swaps them"
                    print(description)
                    print(array)
                    print(pointer)
                (array[j], array[j + 1]) = (array[j + 1], array[j])
                if(showme == True):
                    print(array)
                    printspace(pointer)
            else:
                if showme == True:
                    print(str(array[j])+" is not greater than "+str(array[j+1])+".")
                    print(array)
                    printspace(pointer)
            arrayatprevj = array[j+1]
        
    return array                 

    
show = True
arr = [6,50,400,30,2,1]
print(bubbleSort(arr, show))