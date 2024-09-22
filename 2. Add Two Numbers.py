# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        idx = ans
        flag = 0
        tmp_sum = 0
        while (True):
            if (l1 != None and l2 != None):
                tmp_sum = l1.val + l2.val + flag
                l1 = l1.next
                l2 = l2.next
            elif (l1 != None):
                tmp_sum = l1.val + flag
                l1 = l1.next
            elif (l2 != None):
                tmp_sum = l2.val + flag
                l2 = l2.next
            elif (flag == 1):
                tmp_sum = flag
            else:
                break
            a = tmp_sum % 10
            flag = int(tmp_sum / 10)
            idx.next = ListNode(a, None)
            idx = idx.next
            tmp_sum = 0
        return ans.next
