from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l<r:
            if nums[l]<nums[r]:
                return nums[l]
            mid=(l+r)//2
            if nums[r]<nums[mid]:
                l=mid+1
            else:
                r=mid
        return nums[l]





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