# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        stk = [root]
        map = {None: (0,0)}

        while stk:
            curr = stk[-1]

            if curr.left and curr.left not in map:
                stk.append(curr.left)
            elif curr.right and curr.right not in map:
                stk.append(curr.right)
            else:
                node = stk.pop()
                leftHeight, leftDiameter = map[node.left]
                rightHeight, rightDiameter = map[node.right]

                map[node] = (1+max(leftHeight,rightHeight), max(leftHeight + rightHeight, leftDiameter, rightDiameter))
        return map[root][1]