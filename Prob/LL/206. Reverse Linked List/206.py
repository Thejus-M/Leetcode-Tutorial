from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def from_list(lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        current = head
        for value in lst[1:]:
            current.next = ListNode(value)
            current = current.next
        return head

    def to_list(self):
        lst = []
        current = self
        while current:
            lst.append(current.val)
            current = current.next
        return lst

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        prev,curr=head,head.next
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
        head = ListNode.from_list(lst)
        obj = Solution()
        reversed_head = obj.reverseList(head)
        result = reversed_head.to_list() if reversed_head else []
        
        status = "✅ Correct" if result == expected else "❌ Incorrect"
        print(f"Input: {lst}\nExpected: {expected}\nResult: {result}\nStatus: {status}\n")
        assert result == expected, f"expected {expected}, but got {result}"



if __name__ == "__main__":
    main()