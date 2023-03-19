from typing import List
class Solution:
    def getDistinctDifference(self, N : int, A : List[int]) -> List[int]:
        ans = list(A)
        left = list(A)
        right = list(A)
        left_set = set()
        right_set = set()
        for i in range(N):
            left[i] = len(left_set)
            left_set.add(A[i])
        for i in range(N-1,-1,-1):
            # print(i)
            right[i] = len(right_set)
            right_set.add(A[i])
            
        for i in range(N):
            ans[i] = left[i]-right[i]
        return ans
        
#{ 
 # Driver Code Starts
# class IntArray:

#     def __init__(self) -> None:
#         pass
    
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        A=[int(i) for i in input().split()]
        
        obj = Solution()
        res = obj.getDistinctDifference(N, A)
        
        print(*res)
        

# } Driver Code Ends
