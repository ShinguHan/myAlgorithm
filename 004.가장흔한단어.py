# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라
# 대소문자 구분을 하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다.

import collections
import re

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

commons = collections.defaultdict(int)

filter = [
    word
    for word in re.sub(r"[^\w]", " ", paragraph).lower().split()
    if word not in banned
]
print(filter)
print(max(filter.count()))
