#User function Template for python3
import math  
class Solution:
    def minimumSquares(self, L, B):
        # code here
        k = int(math.gcd(L,B))
        n = int((L/k) * (B/k))
        return [n,k]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        L, B = [int(x) for x in input().split()]
        
        ob = Solution();
        N, K = ob.minimumSquares(L, B)
        print(N,end=" ")
        print(K)
# } Driver Code Ends
