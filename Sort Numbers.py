def solution(nums):
    if hasattr(nums, "__len__"):
        return sorted(nums)
    else:
        return []

print(solution([1,2,3,10,5]))

