class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(start: int, combination: List[int], current_sum: int):
            if current_sum == target:
                result.append(combination[:])
                return

            for i in range(start, len(candidates)):
                # Prune tree: since array is sorted, remaining elements will exceed target
                if current_sum + candidates[i] > target:
                    break

                # Skip duplicate elements at the same depth
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                combination.append(candidates[i])
                backtrack(i + 1, combination, current_sum + candidates[i])
                combination.pop()

        backtrack(0, [], 0)
        return result