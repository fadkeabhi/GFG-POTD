#User function Template for python3

class Solution:
    def appleSequences(self, n, m, arr):
        left, ans = 0, 0
        for right in range(n):
            if arr[right] == 'O':
                m -= 1
                
            while left <= right and m < 0:
                if arr[left] == 'O':
                    m += 1
                left += 1
            ans = max(ans, right-left+1)
        return ans
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        temp = input().split()
        N = int(temp[0])
        M = int(temp[1])
        arr = input()

        ob = Solution()
        print(ob.appleSequences(N, M, arr))

# } Driver Code Ends
