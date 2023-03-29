//{ Driver Code Starts
//Initial Template for C++
#include<bits/stdc++.h>
using namespace std;

// } Driver Code Ends
//User function Template for C++
class Solution
{
    public:
    int isUpper(char a)
    {
        if(a<95)
        return 1;
        return 0;
    }
    
    int countSubstring(string S)
    {
        int s,u,count=0;
        for(int i=0;i<S.length();i++)
        {
            s=0;
            u=0;
            for(int j=i;j<S.length();j++)
            {
                if(isUpper(S[j]))
                {
                    u++;
                }
                else
                {
                    s++;
                }
                if(u==s)
                {
                    count++;
                }
            }
        }
        return count;
    }
};

//{ Driver Code Starts.
int main()
{

    int t;
    cin>>t;
    while(t--)
    {
        string S;
        cin>>S;
        Solution obj;
        cout<<obj.countSubstring(S)<<endl;
    }
}  
// } Driver Code Ends
