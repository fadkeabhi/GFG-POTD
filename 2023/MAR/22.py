#User function Template for python3

class Solution:
        def solve (self, X, Y, S):
            if X>=Y: order = [('pr', X), ('rp', Y)]
            else: order = [('rp', Y), ('pr', X)]
            ans = 0
            for (c0, c1), score in order:
                N, NS = len(S), []
                for i in range(N):
                    NS.append(S[i])
                    if S[i] == c1 and len(NS)>1 and NS[-2]==c0:
                        ans += score
                        NS.pop(); NS.pop()
                S = NS
            return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        str = input().split()
        X = int(str[0])
        Y = int(str[1])
        S = input()
        

        ob = Solution()
        print(ob.solve(X,Y,S))
# } Driver Code Ends
