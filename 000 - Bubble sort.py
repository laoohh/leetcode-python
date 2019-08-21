def bubblesort():
    nums=input("bubblesort::::please input numbers split by space: ")
    mylist = [int(v) for v in nums.split()]
    changes = passes = 0
    last = len(mylist)
    swapped = True
    print("Original List: ", ','.join(map(str, mylist)) )
    while swapped:
        swapped = False
        for j in range(1, last):
            if mylist[j - 1] < mylist[j]:
                mylist[j], mylist[j - 1] = mylist[j - 1],mylist[j]  # Swap
                changes += 1
                swapped = True
                last = j
        if swapped:
            passes += 1
            print('Pass', passes, ':' , ','.join(map(str, mylist)))

    print("\nOriginal List: ", nums )
    print("Sorted List: ", ','.join(map(str, mylist)))
    print("Number of passes =",passes)
    print("Number of changes =",changes)
    return mylist

def bubblesort2():
    nums=input("please input numbers split by space: ")
    mylist = [int(v) for v in nums.split()]

    last = len(mylist)
    swapped = True

    while swapped:
        swapped = False
        for j in range(1, last):
            if mylist[j - 1] > mylist[j]:
                mylist[j], mylist[j - 1] = mylist[j - 1], mylist[j]  # Swap
                swapped = True
                last = j
    return mylist

def bubblesort3():
    nums=input("please input numbers split by space: ")
    mylist = [int(v) for v in nums.split()]

    last = len(mylist)
    swapped = True

    while swapped:
        swapped = False
        for j in range(1, last):
            if mylist[j - 1] < mylist[j]:
                mylist[j], mylist[j - 1] = mylist[j - 1], mylist[j]  # Swap
                swapped = True
                last = j
    return mylist

def bubblesort4():
    nums=input("bubblesort4:::please input numbers split by space: ")
    mylist = [int(v) for v in nums.split()]
    changes = passes = 0
    n = len(mylist)
    swapped = True
    print("Original List: ", ','.join(map(str, mylist)) )
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if mylist[j] < mylist[j+1] :
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
                changes += 1
                swapped = True
        passes += 1
        print('Pass', passes, ':' , ','.join(map(str, mylist)))
        if not swapped:
            break

    print("\nOriginal List: ", nums )
    print("Sorted List: ", ','.join(map(str, mylist)))
    print("Number of passes =",passes)
    print("Number of changes =",changes)
    return mylist

print(bubblesort())
print(bubblesort4())
