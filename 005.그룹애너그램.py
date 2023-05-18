# 문자열 배열을 받아 애너그램 단위로 그룹핑하라

import collections

input = ["eat", "tea", "tan", "ate", "nat", "bat"]


def anegram(input: list[str]) -> list[list[str]]:
    result = collections.defaultdict(list)

    for word in input:
        print(sorted(word))
        result["".join(sorted(word))].append(word)

    return list(result.values())


print(anegram(input))
