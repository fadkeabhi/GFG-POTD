//{ Driver Code Starts
//Initial Template for C++
#include <bits/stdc++.h>
using namespace std;
#define MAX_HEIGHT 100000

// Tree Node
struct Node {
    int data;
    Node *right;
    Node *left;

    Node(int x) {
        data = x;
        right = NULL;
        left = NULL;
    }
};

Node *insert(Node *tree, int val) {
    Node *temp = NULL;
    if (tree == NULL) return new Node(val);

    if (val < tree->data) {
        tree->left = insert(tree->left, val);
    } else if (val > tree->data) {
        tree->right = insert(tree->right, val);
    }

    return tree;
}


// } Driver Code Ends
//User function Template for C++

class Solution{
public:
    long long int Up = 0;
    int target;
    Node * ptr;

    void UpSum(Node * root)
    {
        if(root==NULL)
        Up = -1;
        else if(root->data < target)
        {
            //right
            Up += root->data;
            UpSum(root->right);
        }
        else if(root->data > target)
        {
            //left
            Up += root->data;
            UpSum(root->left);
        }
        else if(root->data == target)
        {
            ptr = root;
        }
    }
    
    long long int DownSum(Node * root)
    {
        if(root==NULL)
        return 0;
        
        long long int left = DownSum(root->left);
        long long int right = DownSum(root->right);
        
        if(left==0)
        {
            return right+root->data;
        }
        if(right==0)
        {
            return left+root->data;
        }
        
        
        if(left<right)
            return left + root->data;
        return right + root->data;
        
    }

    int maxDifferenceBST(Node *root,int target){
        this->target = target;
        UpSum(root);
        if(Up == -1)
        return -1;
        
        long long int Down = DownSum(ptr)-target;
        return Up-Down;
        
    }
};

//{ Driver Code Starts.

int main() {
    int T;
    cin >> T;
    while (T--) {
        Node *root = NULL;

        int N;
        cin >> N;
        for (int i = 0; i < N; i++) {
            int k;
            cin >> k;
            root = insert(root, k);
        }

        int target;
        cin >> target;
        Solution ob;
        cout << ob.maxDifferenceBST(root, target);
        cout << endl;
    }
}
// } Driver Code Ends
