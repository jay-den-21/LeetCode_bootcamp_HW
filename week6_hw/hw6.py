"""Homework 6 solutions: LCA in a binary tree and Top K Frequent Elements."""
from collections import Counter
from typing import List, Optional


class TreeNode:
    """Binary tree node used by the LCA problem."""

    def __init__(self, x: int):
        self.val = x
        self.left: Optional["TreeNode"] = None
        self.right: Optional["TreeNode"] = None


class LowestCommonAncestorSolution:
    """236. Lowest Common Ancestor of a Binary Tree"""

    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: TreeNode, q: TreeNode
    ) -> Optional[TreeNode]:
        if root is None or root is p or root is q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        return left if left else right


class TopKFrequentElementsSolution:
    """347. Top K Frequent Elements"""

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]

        for num, count in freq.items():
            buckets[count].append(num)

        result: List[int] = []
        for count in range(len(nums), 0, -1):
            for num in buckets[count]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
