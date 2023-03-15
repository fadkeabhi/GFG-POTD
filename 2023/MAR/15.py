#User function Template for python3

class Solution():
    def specialPalindrome(self, s1, s2):
        n1, n2 = len(s1), len(s2)
        
        ans = float('inf')
        for i in range(n1-n2+1):
            costs = 0
            for k in range(n2):
                if s1[i+k] != s2[k]:
                    costs += 1
            
            j1, j2 = 0, n1-1
            while j1 < j2:
                if i <= j1 < i+n2 and i <= j2 < i+n2 and s2[j1-i] != s2[j2-i]:
                    break
                left = s1[j1]
                if i <= j1 < i+n2:
                    left = s2[j1-i]
                right = s1[j2]
                if i <= j2 < i+n2:
                    right = s2[j2-i]
                if left != right:
                    costs += 1
                j1 += 1
                j2 -= 1
            else:
                ans = min(ans, costs)
        return -1 if ans == float('inf') else ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        s1, s2 = input().split()
        obj = Solution()
        print(obj.specialPalindrome(s1, s2))
# } Driver Code Ends
