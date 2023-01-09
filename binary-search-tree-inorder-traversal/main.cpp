#include <vector>

using namespace std;

// Definition for a binary tree node.
 struct TreeNode {
     int val;
     TreeNode *left;
     TreeNode *right;
     TreeNode() : val(0), left(nullptr), right(nullptr) {}
     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 };
 
class Solution {
public:
    vector<int> ordered;
    vector<int> inorderTraversal(TreeNode* root) {
        getNum(root);
        return ordered;
    }

    void getNum(TreeNode* root) {
        if (root) {
            getNum(root->left);
            ordered.push_back(root->val);
            getNum(root->right);
        }
    }
};
