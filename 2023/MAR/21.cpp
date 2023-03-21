//{ Driver Code Starts
//Initial Template for C++

#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution{
public:
    int minimumTime(int N,int cur,vector<int> &pos,vector<int> &time){
        int tt[N] ;
        int temp;
        for(int i=0;i<N;i++)
        {
            temp = (pos[i]-cur)*time[i];
            if(temp==0)
            {
                return 0;
            }
            else if(temp > 0)
            {
                tt[i] = temp;
            }
            else
            {
                tt[i] = -temp;
            }
        }
        
        int min = tt[0];
        
        for(int i=0;i<N;i++)
        {
            if(tt[i]<min)
            {
                min = tt[i];
            }
        }
        
        return min;
        
        
        
    }
};

//{ Driver Code Starts.

int main(){
    int t;
    cin>>t;
    while(t--){
        int N,cur;
        cin>>N>>cur;
        vector<int> pos(N),time(N);
        for(int i=0;i<N;i++){
            cin>>pos[i];
        }
        for(int i=0;i<N;i++){
            cin>>time[i];
        }
        Solution ob;
        cout<<ob.minimumTime(N,cur,pos,time)<<endl;
    }
}
// } Driver Code Ends
