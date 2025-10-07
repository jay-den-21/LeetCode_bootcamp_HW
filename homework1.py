# 167. Two Sum II - Input Array Is Sorted
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s == target:
                # Return 1-indexed positions
                return [l + 1, r + 1]
            if s < target:
                l += 1
            else:
                r -= 1
        # Problem guarantees exactly one solution, so this won't be hit.
        return [-1, -1]

# 238. Product of Array Except Self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n

        # prefix products
        pref = 1
        for i in range(n):
            ans[i] = pref
            pref *= nums[i]

        # suffix products
        suff = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= suff
            suff *= nums[i]

        return ans

# 75. Sort Colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Rearrange nums in-place so 0s, then 1s, then 2s.
        Invariants:
          [0..low-1] = 0,  [low..mid-1] = 1,  [mid..high] = unknown,  [high+1..] = 2
        """
        low = mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1