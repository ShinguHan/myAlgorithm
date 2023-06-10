# 정렬되어 있는 두 연결 리스트를 합쳐라

input = [[1, 2, 4], [1, 3, 4]]


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


l1 = [ListNode(lst) for lst in input[0]]
l2 = [ListNode(lst) for lst in input[1]]

try:
    for idx, lst in enumerate(l1):
        lst.next = l1[idx + 1]
except:
    pass

try:
    for idx, lst in enumerate(l2):
        lst.next = l2[idx + 1]
except:
    pass


class solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.mergeTwoLists(l1.next, l2)
        return l1


sol = solution()


result = sol.mergeTwoLists(l1[0], l2[0])

while result:
    print(result.val)
    result = result.next
