# 연결 리스트가 팰린드롬 구조인지 판별하라

from typing import List

input = [1, 2, 2, 1]


class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None


lists = [ListNode(lst) for lst in input]

for idx, lst in enumerate(lists):
    try:
        lst.next = lists[idx + 1]
    except:
        print("마지막")


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        q: List = []

        if not head:
            return True

        node = head

        # 리스트 변환
        while node is not None:
            q.append(node.val)
            node = node.next

        # 팰린드롬 판별
        while len(q) > 1:
            if q.pop(0) != q.pop():
                return False

        return True


re = Solution()

print(re.isPalindrome(lists[0]))
