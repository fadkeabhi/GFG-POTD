#User function Template for python3
class Solution:
    def maxPossibleValue(self, N, A, B):
        ans=0
        c=0
        mi=10**10
        for i in range(N):
            if B[i]//2>0:
                ans+=2*(B[i]//2)*A[i]
                c+=B[i]//2
                mi=min(mi,A[i])
        if c%2==1:
            ans-=2*mi
        return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input().strip())
        A = list(map(int, input().strip().split()))
        B = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxPossibleValue(N, A, B)
        print(ans)

# } Driver Code Ends
