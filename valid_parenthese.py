class Solution:

    def isValid(self, s):
        stack = []
        mapping = {"]":"[", "}":"{", ")":"("}

        for char in s:
            if char in mappings.values():
                stack.append(char)
            elif char in mappings.keys():
                if mapping[char] != stack.pop() or stack == []:
                    return False
        return stack == []