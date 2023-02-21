#User function Template for python3

class Solution:
    def minIteration(self, N, M, x, y):
        x = x-1
        y = y-1
        N=N-1
        M=M-1
        a = max((x+y),((N-x) + (M-y)))
        b = max((x+(M-y)),((N-x)+y))
        return max(a,b)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N, M = map(int,input().split())
		x, y = map(int,input().split())
		ob = Solution()
		print(ob.minIteration(N, M, x, y))
# } Driver Code Ends
