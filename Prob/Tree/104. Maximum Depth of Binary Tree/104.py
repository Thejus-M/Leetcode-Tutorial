from typing import Optional
from my_utils import TreeNode

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        
        dl = self.maxDepth(root.left)
        dr = self.maxDepth(root.right)
        md = max(dl,dr)
        return md + 1

def main():
    inputs = [
        ([3,9,20,None,None,15,7], 3),
        ([1,None,2], 2),
        ([], 0),
        ([0], 1),
        ([1,2,3,4,5,None,6,7,None,None,None,None,8], 4),
    ]

    for vals, expected in inputs:
        # Create binary tree
        if not vals:
            root = None
        else:
            nodes = [TreeNode(val) if val is not None else None for val in vals]
            for i in range(len(nodes)):
                if nodes[i] is not None:
                    if 2*i + 1 < len(nodes):
                        nodes[i].left = nodes[2*i + 1]
                    if 2*i + 2 < len(nodes):
                        nodes[i].right = nodes[2*i + 2]
            root = nodes[0]

        obj = Solution()
        result = obj.maxDepth(root)

        status = "✅ Correct" if result == expected else "❌ Incorrect"
        print(f"Input: vals={vals}\nExpected: {expected}\nResult: {result}\nStatus: {status}\n")
        assert result == expected, f"expected {expected}, but got {result}"

if __name__ == "__main__":
    main()