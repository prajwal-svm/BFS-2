# 199. Binary Tree Right Side View

# Time Complexity: O(n)
# Space Complexity: O(n)
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No

# BFS Intuition:
# Use a queue to traverse the tree level by level.
# Keep track of the rightmost node in each level and add it to the result list      .
# Return the result list.

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        result = []
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                node = queue.popleft()
                if i == size - 1:
                    result.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return result
    
    
# DFS Intuition:
# Use a recursive function to traverse the tree.
# Use a depth variable to keep track of the depth of the current node.
# Overwrite the result list with the rightmost node in each level.
# Traverse the left subtree before the right subtree.

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        def dfs(root, level, result):
            if root is None:
                return []

            if level == len(result):
                result.append(root.val)
            else:
                result[level] = root.val

            dfs(root.left, level+1, result)
            dfs(root.right, level+1, result)
            
        result = []
        dfs(root, 0, result)
        return result