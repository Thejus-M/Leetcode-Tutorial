from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right = 0,len(nums)-1
        while left<right:
            if nums[left]<nums[right]:
                return nums[left]
            mid=(left+right)//2
            if nums[right]<nums[mid]:
                left=mid+1
            else:
                right=mid
        return nums[left]





if __name__ == "__main__":
    inputs = [
        ([3,4,5,1,2], 1),
        ([4,5,6,7,0,1,2], 0),
        ([11,13,15,17], 11),
    ]
    
    s = Solution()
    
    for inp, expected in inputs:
        result = s.findMin(inp)
        status = "✅ Correct" if result == expected else "❌ Incorrect"
        print(f"Input: {inp}\nExpected: {expected}\nResult: {result}\nStatus: {status}\n")
        assert result == expected, f"expected {expected}, but got {result}"