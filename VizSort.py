
import pygame 
import random
import tkinter as tk


r = tk.Tk() 
r.title('SortViz Controller')
r.geometry('900x900')
v = tk.IntVar()
v.set(150)
tbox = tk.Entry(r,width=15,textvariable=v)    #sets up start screen
v2 = tk.IntVar()
v2.set(5)
tbox2 = tk.Entry(r,width=15,textvariable=v2)    #sets up start screen
tbox2.grid(column=1,row=2)
tbox.grid(column=1, row=1)
txt = tk.Label(r, text = "Sorting Method:")
txt.grid(column=0, row=0)
txt2 = tk.Label(r, text = "Array Size:")
txt2.grid(column=0, row=1)
txt3 = tk.Label(r, text = "Speed(in ms)")
txt3.grid(column=0, row=2)

OptionList = [
"Bubble Sort",
"Merge Sort",
"Selection Sort",
"Insertion Sort",
"Quicksort"
]
variable = tk.StringVar(r)
variable.set(OptionList[2])

opt = tk.OptionMenu(r, variable, *OptionList)
opt.config(width=10, font=('Helvetica', 12))
opt.grid(column=1,row=0)

numcomparisons = 0
def onClick():
    run = True
    size = (v.get())
    speed = (v2.get())
    print(size)
    screen = pygame.display.set_mode((1800, 1300)) 
    pygame.font.init()
    pygame.display.set_caption("SortViz") 
    # Window size 
    width = 1800
    length = 1200
    array =[0]*(size+1)
    arr_clr =[(13, 224, 10)]*(size+1)
    clr_ind = 0
    clr =[(0, 0, 12), (255, 155, 0), 
    (0, 20, 153), (123, 123, 123)] 
    fnt = pygame.font.SysFont("comicsans", 50) 
    fnt1 = pygame.font.SysFont("comicsans", 40) 
    # Generate new Array 
    
    def colorwalk():
        for i in range(0,(size+1)):
            arr_clr[i] = clr[2]
            refill()
            arr_clr[i] = clr[3]
    
    def generate_arr(): 
        for i in range(1, (size+1)): 
            arr_clr[i]= clr[0] 
            array[i]= random.randrange(1, 100) 
   
    generate_arr()
    
    
    def refill(): 
        screen.fill((255, 255, 255)) 
        draw() 
        pygame.display.update() 
        pygame.time.delay(speed)

# Sorting Algo:Merge sort 
    def mergesort(array, l, r):
        global numcomparisons
        mid =(l + r)//2
        if l<r:
            numcomparisons+=1
            mergesort(array, l, mid) 
            mergesort(array, mid + 1, r) 
            merge(array, l, mid, 
                mid + 1, r)
            
            
    def merge(array, x1, y1, x2, y2):
        global numcomparisons
        i = x1 
        j = x2 
        temp =[] 
        pygame.event.pump() 
        while i<= y1 and j<= y2:
            pygame.event.pump()
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    return 0
            arr_clr[i]= clr[1] 
            arr_clr[j]= clr[1] 
            refill() 
            arr_clr[i]= clr[0] 
            arr_clr[j]= clr[0]
            numcomparisons+=1
            if array[i]<array[j]: 
                    temp.append(array[i]) 
                    i+= 1
            else: 
                    temp.append(array[j]) 
                    j+= 1
        while i<= y1: 
            arr_clr[i]= clr[1] 
            refill() 
            arr_clr[i]= clr[0] 
            temp.append(array[i])
            numcomparisons+=1
            i+= 1
        while j<= y2: 
            arr_clr[j]= clr[1] 
            refill() 
            arr_clr[j]= clr[0] 
            temp.append(array[j])
            numcomparisons+=1
            j+= 1
        j = 0   
        for i in range(x1, y2 + 1): 
            pygame.event.pump() 
            array[i]= temp[j] 
            j+= 1
            arr_clr[i]= clr[2] 
            refill() 
            if y2-x1 == len(array)-2: 
                arr_clr[i]= clr[3] 
            else: 
                arr_clr[i]= clr[0] 


# Draw the array values 
    def draw(): 
        txt = fnt.render("Press"
        " 'SPACE' to sort.", 2, (0, 0, 0)) 
        screen.blit(txt, (20, 10)) 
        txt1 = fnt.render("Press 'N' to generate an array.", 
                        1, (0, 0, 0)) 
        screen.blit(txt1, (20, 50)) 
        txt2 = fnt1.render(variable.get(), 1, (0, 0, 0)) 
        screen.blit(txt2, (1600, 40))
        txt2 = fnt1.render("Number of Comparisons: "+str(numcomparisons), 1, (0, 0, 0)) 
        screen.blit(txt2, (1000, 40)) 
        element_width =(int(width-(size)))//size
        boundry_arr = 1800 / size
        boundry_grp = 1300 / 100
        pygame.draw.line(screen, (0, 0, 0), 
                        (0, 95), (1800, 95), 6) 
        for i in range(1, 100): 
            pygame.draw.line(screen, 
                            (224, 224, 224), 
                            (0, boundry_grp * i + 100), 
                            (1800, boundry_grp * i + 100), 1) 
    
        for i in range(1, (size+1)): 
            pygame.draw.line(screen, arr_clr[i],
                (boundry_arr * i-3, 100),
                (boundry_arr * i-3, array[i]*boundry_grp + 100),
                element_width)
        
        
    def bubbleSort(array):
        for i in range(len(array)):
            for j in range(0, len(array) - i - 1):
                pygame.event.pump()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: 
                        return 0
                if array[j] > array[j + 1]:
                    arr_clr[j]= clr[1] 
                    arr_clr[j+1]= clr[1] 
                    refill() 
                    arr_clr[j]= clr[0] 
                    arr_clr[j+1]= clr[0] 
                    (array[j], array[j + 1]) = (array[j + 1], array[j])
                    global numcomparisons
                    numcomparisons+=1
        colorwalk()
    
    
    def selectionSort(array, size):
        global numcomparisons
        for step in range(size+1):
            min_idx = step

            for i in range(step + 1, size+1):
                pygame.event.pump()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: 
                        return 0
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
                if array[i] < array[min_idx]:
                    arr_clr[i] = clr[1]
                    arr_clr[min_idx] = clr[1]
                    refill()
                    arr_clr[i] = clr[0]
                    arr_clr[min_idx] = clr[0]
                    min_idx = i
                    numcomparisons+=1
            (array[step], array[min_idx]) = (array[min_idx], array[step])
        colorwalk()
   
   
    def partition(array, low, high):
        global numcomparisons
    # Select the pivot element
        pivot = array[high]
        i = low - 1

    # Put the elements smaller than pivot on the left and greater 
    #than pivot on the right of pivot
        for j in range(low, high):
            pygame.event.pump()
            for event in pygame.event.get():
                 if event.type == pygame.QUIT: 
                     return 0
            if array[j] <= pivot:
                arr_clr[j] = clr[1]
                arr_clr[high] = clr[1]
                refill()
                arr_clr[j] = clr[0]
                arr_clr[high] = clr[0]
                i = i + 1
                (array[i], array[j]) = (array[j], array[i])
                numcomparisons+=1

        (array[i + 1], array[high]) = (array[high], array[i + 1])
        return i + 1
    
    
    def insertionSort(array):

        for step in range(1, len(array)):
            global numcomparisons
            key = array[step]
            j = step - 1
        
        # Compare key with each element on the left of it until an element smaller than it is found
        # For descending order, change key<array[j] to key>array[j].        
            while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                numcomparisons+=1
                j = j - 1
                arr_clr[j] = clr[1]
                arr_clr[j+1] = clr[1]
                refill()
                arr_clr[j] = clr[0]
                arr_clr[j+1] = clr[0]   
        # Place key at after the element just smaller than it.
            array[j + 1] = key
        colorwalk()
    
    
    def quickSort(array, low, high):
        if low < high:
        # Select pivot position and put all the elements smaller 
        # than pivot on left and greater than pivot on right
            pi = partition(array, low, high)

        # Sort the elements on the left of pivot
            quickSort(array, low, pi - 1)

        # Sort the elements on the right of pivot
            quickSort(array, pi + 1, high)
    while run:
        screen.fill((255, 255, 255)) 
        for event in pygame.event.get():
            global numcomparisons
            if event.type == pygame.QUIT: 
                run = False
                numcomparisons = 0
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_n: 
                    generate_arr()
                    numcomparisons = 0
                if event.key == pygame.K_SPACE:
                    if (variable.get()=="Merge Sort"):
                        mergesort(array, 1, len(array)-1)
                    elif (variable.get()=="Bubble Sort"):
                        bubbleSort(array)
                    elif (variable.get()=="Selection Sort"):
                        selectionSort(array, size)
                    elif (variable.get()=="Insertion Sort"):
                        insertionSort(array)
                    elif (variable.get()=="Quicksort"):
                        quickSort(array, 0, size)
                        colorwalk()
        draw()
        pygame.display.update() 

    pygame.quit()
button = tk.Button(r, text='Begin', width=5, bg = 'purple', fg = 'white', command=onClick) 
button.grid(column=0, row=3)
r.mainloop()