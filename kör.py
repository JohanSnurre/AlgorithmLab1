

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
    counter = 0
    print(A)
    for j in range(1,len(A)):
        key = A[j]
        i = j-1;
        while(i>=0 and A[i]>key):
            counter = counter+1
            
            A[i+1] = A[i]
            i-= 1

        A[i+1] = key
        print(A)
    print(counter)


def bSort(A):
    ind = 1
    while(ind < len(A)):
        leftBound = 0
        rightBound = ind


        
        while(leftBound < rightBound):
            mid = (leftBound + rightBound)//2
            if(A[ind] < A[mid]):
                rightBound = mid
                

            else:
                leftBound = mid +1
                
                
       
        newInd = ind
        while(leftBound < newInd):
            elem = A[newInd]
            A[newInd] = A[newInd - 1]
            newInd -= 1
            A[newInd] = elem

        ind+=1
       
    return A





def merge(left,right):
    leftSize = len(left)
    rightSize = len(right)

    newList = []

    while(leftSize > 0 or rightSide > 0):
        if(left[leftSize] > right[rightSize]):
            newList.append(left[leftSize])

        




        

    

def mergeSort(A):
    if(len(A)==1):
        return A


    leftSide = A[0:len(A)/2]
    rightSide = A[len(A)/2:len(A)-1]

    



















    
    
