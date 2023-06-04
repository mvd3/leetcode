class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0 # min
        j = len(numbers) - 1 # max
        while numbers[i] + numbers[j] != target:
            if numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1
        return [i + 1, j + 1]