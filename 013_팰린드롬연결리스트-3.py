# 연결 리스트가 팰린드롬 구조인지 판별하라

from typing import List, Deque
import collections

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
        rev = None
        slow = fast = head

        # 런너를 이용해 역순 연결 리스트 구성
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next

        if fast:
            slow = slow.next

        # 팬린드롬 여부 확인
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev


re = Solution()

print(re.isPalindrome(lists[0]))
