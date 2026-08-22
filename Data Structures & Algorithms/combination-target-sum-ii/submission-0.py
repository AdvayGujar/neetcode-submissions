class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def combinations(index, combination, total):
            if total == target:
                result.append(combination[:])
                return

            if total > target or index >= len(candidates):
                return

            combination.append(candidates[index])
            combinations(index + 1, combination, total + candidates[index])
            combination.pop()

            dummy = index
            while index < len(candidates) and candidates[dummy] == candidates[index]:
                index += 1

            combinations(index, combination, total)

            return result

        return combinations(0, [], 0)