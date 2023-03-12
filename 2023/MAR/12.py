#User function Template for python3

class Solution:
    def findMaxRow(self, mat, N):
        # Code here
        ans = [0,0]
        for i in range(N):
            j = N-1-ans[-1]
            while(mat[i][j] == 1 and j>=0):
                ans[0] = i
                j-=1
            ans[-1] = N-1-j
        return ans
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        mat = []
        for i in range(n):
            A = [int(x) for x in input().split()]
            mat.append(A)
        ob=Solution()
        ans = []
        ans = ob.findMaxRow(mat, n)
        for i in range(2):
            print(ans[i], end =" ")
        print()
# } Driver Code Ends
