class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        elements = set()
        queue = []
        result = 0
        for i in range(len(s)):
            if s[i] not in elements:
                elements.add(s[i])
                queue.append(s[i])
                result = max(result,len(queue))
            else:
                while queue[0] != s[i]:
                    el = queue.pop(0)
                    elements.remove(el)
                queue.pop(0)
                queue.append(s[i])
                result = max(result,len(queue))
        return result  