class Solution {
public:
    unordered_map<int,int> inorderIndex; // map value -> index in inorder
    
    TreeNode* helper(vector<int>& preorder, int preStart, int preEnd,
                     vector<int>& inorder, int inStart, int inEnd) {
        if (preStart > preEnd || inStart > inEnd) return nullptr;

        TreeNode* root = new TreeNode(preorder[preStart]);
        int mid = inorderIndex[root->val]; // root position in inorder
        int leftSize = mid - inStart;

        root->left = helper(preorder, preStart + 1, preStart + leftSize,
                            inorder, inStart, mid - 1);
        root->right = helper(preorder, preStart + leftSize + 1, preEnd,
                             inorder, mid + 1, inEnd);
        return root;
    }

    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        for (int i = 0; i < inorder.size(); i++) {
            inorderIndex[inorder[i]] = i;
        }
        return helper(preorder, 0, preorder.size() - 1, inorder, 0, inorder.size() - 1);
    }
};
