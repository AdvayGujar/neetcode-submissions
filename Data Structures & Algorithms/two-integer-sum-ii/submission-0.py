class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        forwardPointer = 0
        reversePointer = len(numbers)-1
        isRunning = True

        while isRunning:
            add = numbers[forwardPointer] + numbers[reversePointer]
            if add == target:
                return [forwardPointer+1,reversePointer+1]
            elif add > target:
                reversePointer -= 1
            else:
                forwardPointer += 1