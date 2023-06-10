# 연결 리스트를 뒤집어라.

input = [1, 2, 3, 4, 5, None]


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


l1 = [ListNode(lst) for lst in input]

try:
    for idx, lst in enumerate(l1):
        lst.next = l1[idx + 1]
except:
    pass


class solution:
    def reverseList(self, head: ListNode) -> ListNode:
        node, prev = head, None

        while node:
            next, node.next = node.next, prev
            prev, node = node, next

        return prev


sol = solution()


result = sol.reverseList(l1[0])

while result:
    print(result.val)
    result = result.next
