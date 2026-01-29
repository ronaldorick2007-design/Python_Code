#Defining a function to implement binary search
#Complexity : 
#   Time - O(log N)
#   Space - O(1)

def binarySearch(arr, target):
    #Edge case(Empty Array)
    if not arr:
        return -1

    #Declaring pointers
    left , right = 0, len(arr) - 1

    while left < right:
        #Finding middle index of the array
        mid = (left + right) // 2
        
        #Check whether middle element is target
        if arr[mid] == target:
            return mid + 1      #Absolute position
        
        #If middle element is greater than target
        if arr[mid] > target:
            right = mid - 1     #Move right pointer before middle index

        #Or if middle element is lesser than target
        else:
            left = mid + 1      #Move left pointer after middle index

    #Returning default value to indicate absence of element
    return -1

#Initializing test cases
A = [1,6,5,2,3,7]
k = 5
print(binarySearch(A, k))       #output : 3

A = [1,2,4,5]
k = 3
print(binarySearch(A, k))        #output : -1

A = []
k = 7
print(binarySearch(A, k))       #output : -1


