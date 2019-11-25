import random
import time


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

F = []
G = []
H = []
L = []
for i in range(10000):
    F.append(random.randint(0,10000))
    G.append(random.randint(0,10000))
    H.append(random.randint(0,10000))
    L.append(random.randint(0,10000))
    

    



def penis(A):
    #start = time.time()
    for j in range(1,len(A)):
        key = A[j]
        i = j-1;
        while(i>=0 and A[i]>key):
            A[i+1] = A[i]
            i-= 1
            

        A[i+1] = key

   # end = time.time()
    #print(end-start)
    #return A
    

def bSort(A):
    #start = time.time()
    ind = 1
    #loop over elements [2:n] in A 
    while(ind < len(A)):
        #set right- and left-bounds
        leftBound = 0
        rightBound = ind


        #seek out the correct index to place the element
        while(leftBound < rightBound):
            #counter += 1
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
            #counter += 1
            elem = A[newInd]
            A[newInd] = A[newInd - 1]
            newInd -= 1
            A[newInd] = elem

        ind+=1
        
   
    #end = time.time()
    #print(end-start)
    return A



def merge(left,right):
    leftPt = 0
    rightPt = 0
    newList = []

    while(True):
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

        

    

def mergeSortB(A,k):

    if(len(A) <= 1):
        return A
    
    if(len(A)<=k):
        bSort(A)
        return A
    
    left = mergeSortB(A[:len(A)//2],k)
    right = mergeSortB(A[len(A)//2:],k)

    
    return merge(left,right)


def mergeSortIn(A,k):

    if(len(A) <= 1):
        return A
    
    if(len(A)<=k):
        penis(A)
        return A
    
    left = mergeSortIn(A[:len(A)//2],k)
    right = mergeSortIn(A[len(A)//2:],k)

    
    return merge(left,right)
    




def ms(A,k):
    start = time.time()

    mergeSortIn(A,k)

    end = time.time()

    return (end-start)






def test(O):

    l = (0,1000)

    for i in range(1,100):
        m = ms(O,i)
        if(m>=l[0]):
            l = (m,i)

    return l




def averageK(A):

    t = 0
    for i in range(20):
        g = test(A)
        t += g[1]

    return t//20

def genList(start,stop,step):

    return list(range(start,stop,step))
    








    
    
