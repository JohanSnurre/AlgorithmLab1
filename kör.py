

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
    print(A)
    for j in range(1,len(A)):
        key = A[j]
        i = j-1;
        while(i>=0 and A[i]>key):
            A[i+1] = A[i]
            i-= 1

        A[i+1] = key
        print(A)



    
    
