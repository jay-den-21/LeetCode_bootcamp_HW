from collections import deque
from typing import Deque, List, Optional, Tuple


# 199. Binary Tree Right Side View
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution199:
    def rightSideView(self, root: Optional["TreeNode"]) -> List[int]:
        """
        Level-order traversal that records the last node value seen on each layer.
        """
        if not root:
            return []

        view: List[int] = []
        q: Deque["TreeNode"] = deque([root])

        while q:
            layer_size = len(q)
            for i in range(layer_size):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if i == layer_size - 1:
                    view.append(node.val)
        return view


# 994. Rotting Oranges
class Solution994:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Multi-source BFS starting from all rotten oranges simultaneously.
        """
        rows = len(grid)
        cols = len(grid[0]) if rows else 0

        q: Deque[Tuple[int, int, int]] = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c, 0))
                elif grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while q:
            r, c, minutes = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    q.append((nr, nc, minutes + 1))

        return minutes if fresh == 0 else -1


# 210. Course Schedule II
class Solution210:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Kahn's algorithm (BFS-based topological sort).
        """
        adj: List[List[int]] = [[] for _ in range(numCourses)]
        indegree: List[int] = [0] * numCourses

        for course, pre in prerequisites:
            adj[pre].append(course)
            indegree[course] += 1

        q: Deque[int] = deque(i for i in range(numCourses) if indegree[i] == 0)
        order: List[int] = []

        while q:
            node = q.popleft()
            order.append(node)
            for neighbor in adj[node]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)

        return order if len(order) == numCourses else []
