from typing import Optional
from my_utils import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        s=f=head
        while f and f.next:
            s,f=s.next,f.next.next
            if s==f:
                return True
        return False

def main():
    inputs = [
        ([3,2,0,-4], 1, True),
        ([1,2], 0, True),
        ([1], -1, False),
        ([], -1, False),
        ([1,2,3,4,5], -1, False),
    ]

    for vals, pos, expected in inputs:
        # Create linked list
        head = ListNode(0)
        current = head
        nodes = []
        for val in vals:
            node = ListNode(val)
            nodes.append(node)
            current.next = node
            current = current.next
        head = head.next  # Move to actual head

        # Create cycle if pos is valid
        if pos != -1 and nodes:
            current.next = nodes[pos]

        obj = Solution()
        result = obj.hasCycle(head)

        status = "✅ Correct" if result == expected else "❌ Incorrect"
        print(f"Input: vals={vals}, pos={pos}\nExpected: {expected}\nResult: {result}\nStatus: {status}\n")
        assert result == expected, f"expected {expected}, but got {result}"

if __name__ == "__main__":
    main()