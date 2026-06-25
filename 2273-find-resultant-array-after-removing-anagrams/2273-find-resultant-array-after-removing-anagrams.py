class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []

        for word in words:
            if not ans or sorted(ans[-1]) != sorted(word):
                ans.append(word)

        return ans