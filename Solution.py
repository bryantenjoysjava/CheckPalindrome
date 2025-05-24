class Solution:
    def isPalindrome(self, s: str) -> bool:

        modified_string = ''.join(ch for ch in s if ch.isalnum())
        modified_string = modified_string.lower()
        left = 0
        right = len(modified_string) - 1

        while left < right:

            if modified_string[left] != modified_string[right]:
                return False

            left += 1
            right -= 1

        return True



