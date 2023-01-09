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
    bool hasPathSum(TreeNode* root, int targetSum) {
        vector<int> a;
        return checkSum(root, targetSum, a);
    }

    bool checkSum(TreeNode* root, int targetSum, vector<int> total) {
        if (!root) {
            return false;
        }

        total.push_back(root->val);
        if (!root->left && !root->right) {
            int tot = sum(total);
            if (tot == targetSum) {
                return true;
            }
            return false;
        }
        if (checkSum(root->left, targetSum, total)) {
            return true;
        }
        if (checkSum(root->right, targetSum, total)) {
            return true;
        }
        total.pop_back();
        return false;
    }

    int sum(vector<int>& nums) {
        int total = 0;
        for (int i = 0; i < nums.size(); i++) {
            total += nums[i];
        }
        return total;
    }
};
