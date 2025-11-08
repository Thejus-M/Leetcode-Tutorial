from typing import Optional
from my_utils import ListNode

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return head
        f,s = head,head.next

        while s and s.next:
            f,s=f.next,s.next.next
            
        p2,prv=f.next,None
        f.next=None
        while p2:
            nxt=p2.next
            p2.next=prv
            prv,p2=p2,nxt
        p1,p2=head,prv
        while p2:
            a,b=p1.next,p2.next
            p1.next=p2
            p2.next=a
            p1,p2=a,b
        return head 
        
def main():
    inputs = [
        ([1,2,3,4], [1,4,2,3]),
        ([1,2,3,4,5], [1,5,2,4,3]),
        ([1], [1]),
        ([], []),
        ([1,2], [1,2]),
    ]

    for vals, expected in inputs:
        # Create linked list
        head = ListNode(0)
        current = head
        for val in vals:
            node = ListNode(val)
            current.next = node
            current = current.next
        head = head.next  # Move to actual head

        obj = Solution()
        obj.reorderList(head)

        # Collect result from linked list
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next

        status = "✅ Correct" if result == expected else "❌ Incorrect"
        print(f"Input: vals={vals}\nExpected: {expected}\nResult: {result}\nStatus: {status}\n")
        assert result == expected, f"expected {expected}, but got {result}"

if __name__ == "__main__":
    main()