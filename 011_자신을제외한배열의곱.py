# 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라

input = [1, 2, 3, 4]


def multiply(nums: list[int]) -> list[int]:
    p = 1
    result = []

    for num in nums:
        result.append(p)
        p = p * num

    p = 1
    for index in range(len(nums) - 1, -1, -1):
        result[index] = result[index] * p
        p = p * nums[index]

    return result


print(multiply(input))
