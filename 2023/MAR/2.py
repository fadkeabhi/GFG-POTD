#User function Template for python3

class Solution:
    def minCost(self, costs) -> int:
        from heapq import heappushpop, heappush, heappop
        if len(costs) == 1:
            return min(costs[0])
        if len(costs[0]) == 1:
            return -1
            
        n, k = len(costs), len(costs[0])
        dp = [[0]*k for _ in range(n+1)]
        
        min1, min2 = (0, None), (0, None)
        
        h = []
        for wall in range(n):
            for color in range(k):
                dp[wall+1][color] = (min1[0] if min1[1] != color else min2[0]) + costs[wall][color]
                if len(h) < 2:
                    heappush(h, (-dp[wall+1][color], color))
                else:
                    heappushpop(h, (-dp[wall+1][color], color))
           
            min2 = heappop(h)
            min2 = (min2[0]*(-1), min2[1])
            min1 = heappop(h)
            min1 = (min1[0]*(-1), min1[1])
        return min1[0]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List


class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n, m = map(int, input().split())
        
        
        costs=IntMatrix().Input(n, m)
        
        obj = Solution()
        res = obj.minCost(costs)
        
        print(res)
# } Driver Code Ends
