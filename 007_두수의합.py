# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자 인덱스를 리턴하라

nums = [2, 7, 11, 15]
target = 9


def search_indexes(nums: list[int], target: int) -> list[int]:
    for i, num in enumerate(nums):
        find_num = target - num
        if find_num in nums[i + 1 :]:
            return nums.index(num), nums[i + 1 :].index(find_num) + (i + 1)


print(search_indexes(nums, target))
