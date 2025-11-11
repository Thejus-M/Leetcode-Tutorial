from typing import Optional
from my_utils import ListNode

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        l=r=dummy
        
        for _ in range(n):
            r=r.next
        
        while r.next:
            r=r.next
            l=l.next
        
        l.next=l.next.next
        return dummy.next
    

def main():
    inputs = [
        ([1,2,3,4,5], 2, [1,2,3,5]),
        ([1], 1, []),
        ([1,2], 1, [1]),
        ([1,2], 2, [2]),
        ([1,2,3], 3, [2,3]),
    ]

    for vals, n, expected in inputs:
        # Create linked list
        if not vals:
            head = None
        else:
            head = ListNode(vals[0])
            current = head
            for val in vals[1:]:
                current.next = ListNode(val)
                current = current.next

        obj = Solution()
        result_head = obj.removeNthFromEnd(head, n)

        # Convert result linked list to list for easy comparison
        result = []
        while result_head:
            result.append(result_head.val)
            result_head = result_head.next

        status = "✅ Correct" if result == expected else "❌ Incorrect"
        print(f"Input: vals={vals}, n={n}\nExpected: {expected}\nResult: {result}\nStatus: {status}\n")
        assert result == expected, f"expected {expected}, but got {result}"

if __name__ == "__main__":
    main()