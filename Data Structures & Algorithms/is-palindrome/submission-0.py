class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = "".join(char.lower() for char in s if char.isalnum())
        if filtered_s == filtered_s[::-1]:
            return True
        else:
            return False