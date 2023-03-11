//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


// } Driver Code Ends
class Solution {
  public:
        vector<int> solveQueries(int n, int num, vector<int> &a, vector<vector<int>> &q) {
        // code here
        unordered_map<int,int> mp;
        for(int i=0;i<n;i++){
            int freq=1;
            for(int j=i+1;j<n;j++){
                if(a[i]==a[j]) freq++;
            }
            mp[i]=freq;
        }
        vector<int> ans;
        for(int i=0;i<num;i++){
            int l=q[i][0];
            int r=q[i][1];
            int k=q[i][2];
             int ans2=0;
            for(int j=l;j<=r;j++){
                if(mp[j]==k) ans2++;
            }
            ans.push_back(ans2);
        }
        return ans;
    }
};


//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int N;
        cin>>N;
        int num;
        cin>>num;
        vector<int> A(N);
        for(int i=0;i<N;i++){
            cin>>A[i];
        }
        vector<vector<int>> Q(num, vector<int>(3));
        for(int i=0;i<num;i++){
            for(int j=0;j<3;j++){
                cin>>Q[i][j];
            }
        }
        Solution obj;
        vector<int> res = obj.solveQueries(N, num, A, Q);
        
        for(auto ele:res){
            cout<<ele<<" ";
        }
        cout<<endl;
    }
}

// } Driver Code Ends
