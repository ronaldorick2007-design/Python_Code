def LinearSearch(arr, target):
    #Calculating length of array
    N = len(arr)

    #Iterating through array
    for i in range(N):
        #Checking whether element is the target
        if arr[i] == target:
            return i + 1 #Actual position
    
    #Returning default ,if element not found
    return -1

#Array and target declaration
A = [1,4,6,2,3,5]
k = 6
#Function Call
print( LinearSearch(A, k) )
