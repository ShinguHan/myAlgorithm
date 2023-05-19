import re

input = "A man, a Plan, a canal : Panama"


def palindrome(s: str) -> bool:
    s = re.sub(r"[^\w]", "", input).lower()
    return s == s[::-1]


print(palindrome(input))
