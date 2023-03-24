#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def removeReverse(self, s):
        h,d=[0]*26,1
    
        for i in range(len(s)):
            h[ord(s[i])-97]+=1
            
        i=0
        while(0<=i<len(s)):
            if(h[ord(s[i])-97])>1:
                h[ord(s[i])-97]-=1
                s=s[:i]+s[i+1:]
                i=len(s)-1 if d==1 else 0
                d*=-1
            
            else:
                i+=d
        return s if d>0 else s[::-1]

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        S = input()
        ob = Solution()
        ans = ob.removeReverse(S)
        print(ans)


# } Driver Code Ends
