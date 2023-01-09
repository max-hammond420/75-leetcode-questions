#include <vector>
#include <queue>

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
    vector<vector<int>> levelOrder(TreeNode* root) {
        queue<TreeNode*> queue;
        vector<vector<int>> nodes;

        if (root) {
            queue.push(root);
        }

        while (!queue.empty()) {
            int count = queue.size();
            vector<int> level;

            for (int i = 0; i < count; i++) {
                TreeNode* curr = queue.front();
                queue.pop();

                level.push_back(curr->val);

                if (curr->left != nullptr) {
                    queue.push(curr->left);
                }
                if (curr->right != nullptr) {
                    queue.push(curr->right);
                }
            }
            nodes.push_back(level);
        }

        return nodes;
    }
};
