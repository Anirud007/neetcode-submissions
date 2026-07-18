class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = { 
            "{" : "}",
            "(" : ")",
            "[" : "]"
        }
        for ch in s:
            if ch in mapping:
                stack.append(mapping[ch])
            elif not stack or ch != stack.pop():
                return False

        if len(stack) != 0:
            return False

        return True