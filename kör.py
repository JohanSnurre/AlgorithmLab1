

def insertionSort(my_list):
    # for every element in our array
    for index in range(1, len(my_list)):
        current = my_list[index]
        position = index

        while position > 0 and my_list[position-1] > current:
            my_list[position] = my_list[position-1]
            position -= 1

        my_list[position] = current

    return my_list

my_list = [8,2,1,3,5,4]




def penis(A):
    
    #print(A)
    for j in range(1,len(A)):
        print(A)
        key = A[j]
        i = j-1;
        while(i>=0 and A[i]>key):
            #counter = counter+1
            
            A[i+1] = A[i]
            i-= 1
            print(A)

        A[i+1] = key
        
    #print(counter)
    return A
    #return True

def bSort(A):
    counter = 0
    ind = 1
    #loop over elements [2:n] in A 
    while(ind < len(A)):
        #set right- and left-bounds
        leftBound = 0
        rightBound = ind


        #seek out the correct index to place the element
        while(leftBound < rightBound):
            counter += 1
            mid = (leftBound + rightBound)//2
            #print("left = " + str(leftBound) + ", right = " + str(rightBound))
            if(A[ind] < A[mid]):
                rightBound = mid 
                

            else:
                leftBound = mid +1
                
                
        #moving all elements right of the inserted element
        #one step to the right
        newInd = ind
        while(leftBound < newInd):
            counter += 1
            elem = A[newInd]
            A[newInd] = A[newInd - 1]
            newInd -= 1
            A[newInd] = elem

        ind+=1
        
    #return A
    print (counter)
    return True




def merge(left,right):
    leftPt = 0
    rightPt = 0
    newList = []

    while(leftPt < len(left) or rightPt < len(right)):
        m = min(left[leftPt],right[rightPt])
        newList.append(m)

        if(m == left[leftPt]):
            leftPt += 1
        else:
            rightPt += 1

        if(leftPt == len(left)):
            for i in right[rightPt:]:
                newList.append(i)
            break

        if(rightPt == len(right)):
            for i in left[leftPt:]:
                newList.append(i)
            break

    return newList

        

    

def mergeSort(A,k):
    if(len(A)<=k):
        penis(A)
        return A
    
    left = mergeSort(A[:len(A)//2],k)
    right = mergeSort(A[len(A)//2:],k)

    
    return merge(left,right)
    


















    
    
