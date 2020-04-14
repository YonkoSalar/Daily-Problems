# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at index i of the new array is the product 
# of all the numbers in the original array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would
# be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

A = [1, 2, 3, 4, 5]
n = len(A)

def function(arr, n):

    #Allocate arrays
    left = [0]*n
    right = [0]*n

    #Allocate Memory for product array
    prod = [0]*n

    #Left most element of the left array is always 1
    left[0] = 1

    #Right most element of right arrays is always 1
    right[n-1] = 1

    #Construct left array
    for i in range(1, n):
        left[i] = arr[i-1] * left[i-1]

    #Construct the right array
    for j in range(n-2,-1,-1):
        right[j] = arr[j+1]*right[j+1]

    # Construct the product array using  
    # left[] and right[]  
    for i in range(n):  
        prod[i] = left[i] * right[i]  
  
    # print the constructed prod array  
    for i in range(n):  
        print(prod[i], end =' ') 

print(function(A, n))


        