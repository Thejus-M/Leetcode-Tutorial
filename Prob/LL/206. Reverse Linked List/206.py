from typing import Optional
from my_utils import ListNode, create_linked_list

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        prev,curr=head,head.next
        head.next = None  # Break the link from the original head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev,curr=curr,nxt
        return prev

def main():
    inputs = [
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
        ([], []),
        ([1], [1]),
        ([1, 2, 3], [3, 2, 1]),
    ]

    for lst, expected in inputs:
        head = create_linked_list(lst)
        obj = Solution()
        reversed_head = obj.reverseList(head)
        result = []
        current = reversed_head
        while current:
            result.append(current.val)
            current = current.next
        
        status = "✅ Correct" if result == expected else "❌ Incorrect"
        print(f"Input: {lst}\nExpected: {expected}\nResult: {result}\nStatus: {status}\n")
        assert result == expected, f"expected {expected}, but got {result}"



if __name__ == "__main__":
    main()