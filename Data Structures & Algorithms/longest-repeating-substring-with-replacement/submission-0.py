class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequency = {}
        left = 0
        maxLength = 0

        for right in range(len(s)):
            if s[right] not in frequency:
                frequency[s[right]] = 1
            else:
                frequency[s[right]] += 1

            maxFrequency = max(frequency.values())

            replacementCost = (right - left + 1) - maxFrequency

            if replacementCost <= k:
                maxLength = right - left + 1
            else:
                frequency[s[left]] -= 1
                if not frequency[s[left]]:
                    frequency.pop(s[left])
                left += 1

        return maxLength