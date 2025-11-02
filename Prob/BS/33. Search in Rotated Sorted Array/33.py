from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        pos = -1
        while l<=r:
            m=(l+r)//2
            if nums[m]==target:return m
            if nums[l]<=nums[m]:
                if nums[l]<=target<=nums[m]:
                    r=m-1
                else:
                    l=m+1
            else:
                if nums[m]<=target<=nums[r]:
                    l=m+1
                else:
                    r=m-1
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