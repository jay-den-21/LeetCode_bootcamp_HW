# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # 1) Find middle (slow at mid; if odd length, fast != None)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2) If odd length, skip the middle node
        if fast:                   # odd number of nodes
            slow = slow.next

        # 3) Reverse second half starting at slow
        prev, curr = None, slow
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # 'prev' is head of reversed second half

        # 4) Compare first half and reversed second half
        p1, p2 = head, prev
        while p2:                  # second half is <= first half in length
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next

        return True

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        L0→L1→…→Ln  ⟶  L0→Ln→L1→Ln-1→L2→…
        """
        if not head or not head.next or not head.next.next:
            return

        # 1) Find middle (slow ends at mid-left on even length)
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2) Reverse the second half starting at slow.next
        prev, curr = None, slow.next
        slow.next = None  # split the list into two halves
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        # now: head = first half; prev = head of reversed second half

        # 3) Merge alternately: first, second, first, second, ...
        p1, p2 = head, prev
        while p2:
            n1, n2 = p1.next, p2.next
            p1.next = p2
            p2.next = n1
            p1, p2 = n1, n2


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])

        # Check if first row / first column need to be zeroed
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # Use first row and first column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Zero rows based on markers
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1, n):
                    matrix[i][j] = 0

        # Zero columns based on markers
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        # Zero the first row/column if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

