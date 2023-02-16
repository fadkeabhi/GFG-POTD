//{ Driver Code Starts
//Initial Template for C++
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++
class Solution{
public:
    int dfs(int i, vector<int>& arr, vector<int> &vis)

    {

        int n = arr.size();

        if(i>=n || i<0) return 1;

        if(vis[i]) return vis[i];

        vis[i] = -1;

        int x = dfs(i+arr[i], arr, vis);

        vis[i] = x;

    }

    int goodStones(int n,vector<int> &arr){

        // Cod heree

         vector<int> vis(n);

        int cnt = 0;

        for(int i = 0; i<n; ++i)

        dfs(i, arr, vis);

        for(int i = 0; i<n; ++i) cnt += vis[i]==1;

        return cnt;
    }  
};

//{ Driver Code Starts.

int main(){
    
    int t;
    cin>>t;
    while(t--){
        int n;
        cin>>n;
        vector<int> arr(n);
        for(int i=0;i<n;i++){
            cin>>arr[i];
        }
        Solution ob;
        cout<<ob.goodStones(n,arr)<<endl;
    }
    return 0;
}
// } Driver Code Ends
