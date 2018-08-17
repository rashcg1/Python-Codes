#Function to left rotate arr[] of size n by d*/
def leftRotate(arr,d):
    a1=[]
    a1=arr[d:]+arr[:d]
    return a1
        


 
# utility function to print an array */
def printArray(arr,size):
    for i in range(size):
        print ("%d"% arr[i],end=" ")
 
  
# Driver program to test above functions */
arr = [1, 2, 3, 4, 5, 6, 7]
printArray(arr,len(arr))
print(leftRotate(arr, 2))
