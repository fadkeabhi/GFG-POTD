#User function Template for python3

class Solution:
    def avoidExlosion(self, mix, n, danger, m):
        
        arr = [i for i in range(n+1)]
        def union(i, j):
            r1, r2 = find(i), find(j)
            if r1 != r2:
                arr[r1] = r2
            return r2
        def find(i):
            while i != arr[i]:
                i = arr[i]
            return i
            

        ans = []
        for x, y in mix:
            rx, ry = find(x), find(y)
            for p, q in danger:
                rp, rq = find(p), find(q)
                if (rx, ry) == (rp, rq) or (rx, ry) == (rq, rp):
                    ans.append("No")
                    break
            else:
                union(rx, ry)
                ans.append("Yes")
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        mix = [[0 for _ in range(2)] for _ in range(n)]
        danger = [[0 for _ in range(2)] for _ in range(m)]
        for i in range(n+m):
            if i < n:
                a,b = map(int, input().split())
                mix[i][0] = a
                mix[i][1] = b
            else:
                a,b = map(int, input().split())
                danger[i-n][0] = a
                danger[i-n][1] = b
        
        obj=Solution()
        print(*obj.avoidExlosion(mix, n, danger, m))
        
# } Driver Code Ends
