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
        def reverse(node: ListNode, prev: ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)

        return reverse(head)


sol = solution()


result = sol.reverseList(l1[0])

while result:
    print(result.val)
    result = result.next
