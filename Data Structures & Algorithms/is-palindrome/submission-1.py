class Solution:
    def isPalindrome(self, s: str) -> bool:
        """s=s.lower()
        s=re.sub(r'[^a-zA-Z0-9]', '', s)

        left=0
        right=len(s)-1
        while left<=right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True"""

        new_s="".join(char.lower() for char in s if char.isalnum())
        left=0
        right=len(new_s)-1
        while left<=right:
            if new_s[left]!=new_s[right]:
                return False
            left+=1
            right-=1
        return True