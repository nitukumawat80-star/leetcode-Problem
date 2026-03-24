class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.strip().split()
        rev = x[::-1]
        rev  = " ".join(rev)
        return rev