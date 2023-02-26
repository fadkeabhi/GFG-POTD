//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


// } Driver Code Ends
//User function Template for C++

class Solution {
  public:
    int checkCompressed(string S, string T){
        // code here
        
        int i=0;
        int j=0;
        
        while( j<T.size() ){
            
            if(isalpha(T[j])){
                if (S[i]!=T[j]) return 0;
                  
                i++;
                j++;
            }
            else{
                int num=0;
                while(isdigit(T[j])){
                    num=(num*10 + (T[j]-'0') );
                    j++;
                }
                
                i+=num;
            }
        
        }
        
        return ((i==S.size() && j==T.size())?1:0);
        
    }
        
};


//{ Driver Code Starts.

int main() {
    int t;
    cin >> t;
    while (t--) {
        string S,T;
        
        cin>>S>>T;

        Solution ob;
        cout << ob.checkCompressed(S,T) << endl;
    }
    return 0;
}
// } Driver Code Ends
