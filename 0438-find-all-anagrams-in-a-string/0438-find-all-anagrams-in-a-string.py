from collections import Counter


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need = Counter(p)
        window = Counter()

        left = 0
        right = 0
        ans = []

        while right < len(s):
            window[s[right]] += 1

            if right - left + 1 == len(p):
                if window == need:
                    ans.append(left)

                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1

            right += 1

        return ans
