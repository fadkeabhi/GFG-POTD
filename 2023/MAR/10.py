#User function Template for python3

class Solution:
    def maxTripletProduct (self, arr,  n): 
        arr.sort()
        n1 = arr[0]*arr[1]*arr[2]
        n2 = arr[0]*arr[1]*arr[-1]
        n3 = arr[0]*arr[-2]*arr[-1]
        n4 = arr[-3]*arr[-2]*arr[-1]
        return max(n1, n2, n3, n4)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob=Solution()
    res = ob.maxTripletProduct(arr, n)
    print(res)
# } Driver Code Ends
