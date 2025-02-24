# 993. Cousins in Binary Tree

# Time Complexity: O(n)
# Space Complexity: O(n)
# Did this code successfully run on Leetcode: Yes
# Any problem you faced while coding this: No

# BFS Intuition:
# Use a queue to traverse the tree level by level.
# Keep track of the parent of the current node.
# If the current node has the same value as x or y, check if they are cousins by comparing the depth and parent .
# Return True if they are cousins, False otherwise.

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root:
            return False
        queue = deque([(root, None)])
        while queue:
            size = len(queue)
            x_found = False
            y_found = False
            x_parent = None
            y_parent = None
            for _ in range(size):
                node, parent = queue.popleft()
                if node.val == x:
                    x_found = True
                    x_parent = parent
                if node.val == y:
                    y_found = True
                    y_parent = parent
                if node.left:
                    queue.append((node.left, node))
                if node.right:
                    queue.append((node.right, node))
            if x_found and y_found:
                return x_parent != y_parent
        return False
    
# Alternate BFS:
# update the level and parent of the current node while traversing the node's left and right children.
# if the current node has the same value as x or y, check if they are cousins by comparing the level and parent.
# Return True if they are cousins, False otherwise.

class Solution:
    def __init__(self):
        self.x_level = -1
        self.y_level = -2
        self.x_parent = -1
        self.y_parent = -1

    def updateLevelAndParent(self,parent, node,level, x,y):
        if node.val == x:
            self.x_level = level + 1
            self.x_parent = parent
        if node.val == y:
            self.y_level = level + 1
            self.y_parent = parent

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        
        q = deque([root])

        level = -1
        while q:
            size = len(q)
            level += 1
            for _ in range(size):
                node = q.popleft()
                
                if node.left:
                    self.updateLevelAndParent(node.val, node.left,level,x,y)
                    q.append(node.left)
                if node.right:
                    self.updateLevelAndParent(node.val, node.right,level,x,y)
                    q.append(node.right)

            if self.x_level == self.y_level and self.x_parent != self.y_parent:
                return True

        return False

    
# DFS Intuition:
# Use a recursive function to traverse the tree.
# Keep track of the depth and parent of the current node.
# If the current node has the same value as x or y, check if they are cousins by comparing the depth and parent.
# Return True if they are cousins, False otherwise.

class Solution:
    def __init__(self):
        self.x_level = -1
        self.y_level = -2
        self.x_parent = -1
        self.y_parent = -1

    def dfs(self, parent, node, level, x,y):
        if node is None:
            return

        if node.val == x:
            self.x_level = level
            self.x_parent = parent
        if node.val == y:
            self.y_level = level
            self.y_parent = parent

        self.dfs(node.val, node.left, level+1, x,y)
        self.dfs(node.val, node.right, level+1, x,y)
        

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.dfs(None, root, 0, x,y)
        return self.x_level == self.y_level and self.x_parent != self.y_parent

