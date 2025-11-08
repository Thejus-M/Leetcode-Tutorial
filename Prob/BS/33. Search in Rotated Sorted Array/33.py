from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid
            if nums[left]<=nums[mid]:
                if nums[left]<=target<=nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid]<=target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return -1





if __name__ == "__main__":
    inputs = [
        (([4,5,6,7,0,1,2], 0), 4),
        (([4,5,6,7,0,1,2], 3), -1),
        (([1], 0), -1),
    ]
    
    s = Solution()
    
    for (inp, target), expected in inputs:
        result = s.search(inp, target)
        status = "✅ Correct" if result == expected else "❌ Incorrect"
        print(f"Input: {inp}, Target: {target}\nExpected: {expected}\nResult: {result}\nStatus: {status}\n")
        assert result == expected, f"expected {expected}, but got {result}"