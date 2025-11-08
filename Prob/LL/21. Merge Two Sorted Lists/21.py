from typing import Optional
from my_utils import ListNode, create_linked_list

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and list2:
            return list2
        if list1 and not list2:
            return list1
        res=head=ListNode(0)

        while list1 and list2:
            if list1.val<list2.val:
                head.next=list1
                list1=list1.next
            else:
                head.next=list2
                list2=list2.next
            head=head.next
        if list1 or list2:
            head.next=list1 if list1 else list2
        return res.next

def main():
    inputs = [
        (([1,2,4], [1,3,4]), [1,1,2,3,4,4]),
        (([], []), []),
        (([], [0]), [0]),
        (([2,5,7], [3,11]), [2,3,5,7,11]),
    ]

    for (list1_vals, list2_vals), expected in inputs:
        list1 = create_linked_list(list1_vals)
        list2 = create_linked_list(list2_vals)
        # expected is already correctly assigned

        obj = Solution()
        merged_head = obj.mergeTwoLists(list1, list2)
        
        result = []
        current = merged_head
        while current:
            result.append(current.val)
            current = current.next
        
        status = "✅ Correct" if result == expected else "❌ Incorrect"
        print(f"Input: list1={list1_vals}, list2={list2_vals}\nExpected: {expected}\nResult: {result}\nStatus: {status}\n")
        assert result == expected, f"expected {expected}, but got {result}"

if __name__ == "__main__":
    main()