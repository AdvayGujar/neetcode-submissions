class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def combinations(index, combination, total):
            if total == target:
                result.append(combination[:])
                return
            
            if total > target or index >= (len(candidates)):
                return

            combination.append(candidates[index])
            combinations(index, combination, total + candidates[index])
            combination.pop()
            combinations(index + 1, combination, total)

            return result

        return combinations(0, [], 0)