# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라

nums = [2, 7, 11, 15]
target = 13


def search_indexes(nums: list[int], target: int) -> list[int]:
    key_map = {}
    for i, num in enumerate(nums):
        key_map[num] = i

    for i, num in enumerate(nums):
        if target - num in key_map:
            return key_map[num], key_map[target - num]


print(search_indexes(nums, target))
