#include <queue>
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
    vector<int> rightSideView(TreeNode* root) {
        vector<int> nums;
        queue<TreeNode*> q;

        if (root) {
            q.push(root);
        }
        
        while (!q.empty()) {
            int count = q.size();

            nums.push_back(q.back()->val);

            for (int i = 0; i < count; i++) {
                TreeNode* curr = q.front();
                q.pop();

                if (curr->left) {
                    q.push(curr->left);
                }
                if (curr->right) {
                    q.push(curr->right);
                }
            }
        }
        
        return nums;
    }
};
