class Solution:
    def minSteps(self, str : str) -> int:
        # code here
        count = 1
        for i in range(1, len(str)):
            if(str[i] == str[i-1]):
                continue
            count +=1
        return (count + 2) //2
        



#{ 
 # Driver Code Starts
if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        str = (input())
        
        obj = Solution()
        res = obj.minSteps(str)
        
        print(res)
        

# } Driver Code Ends
