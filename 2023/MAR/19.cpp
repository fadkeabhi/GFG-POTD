//{ Driver Code Starts
#include<bits/stdc++.h>
using namespace std;


class Array
{
public:
    template <class T>
    static void input(vector<T> &A,int n)
    {
        for (int i = 0; i < n; i++)
        {
            scanf("%d ",&A[i]);
        }
    }

    template <class T>
    static void print(vector<T> &A)
    {
        for (int i = 0; i < A.size(); i++)
        {
            cout << A[i] << " ";
        }
        cout << endl;
    }
};


// } Driver Code Ends

class Solution {
  public:
    vector<int> getDistinctDifference(int n, vector<int> &a) {
        // code here
        vector<int> left(n,0);
        vector<int> right(n,0);
        set<int> s1;
        set<int> s2;
        
        s1.insert(a[0]);
        s2.insert(a[n-1]);
        for(int i=1 ; i<n ; i++)
        {
            int j = n-1-i;
            left[i] = s1.size();    s1.insert(a[i]);
            right[j] = s2.size();   s2.insert(a[j]);
        }
        
        vector<int> ans;
        for(int i=0 ; i<n ; i++)
        {
            ans.push_back(left[i]-right[i]);
        }
        return ans;
    }
};


//{ Driver Code Starts.

int main(){
    int t;
    scanf("%d ",&t);
    while(t--){
        
        int N;
        scanf("%d",&N);
        
        
        vector<int> A(N);
        Array::input(A,N);
        
        Solution obj;
        vector<int> res = obj.getDistinctDifference(N, A);
        
        Array::print(res);
        
    }
}

// } Driver Code Ends
