class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        dic = {}
        for i in range (len(s)):
            dic[indices[i]] = s[i]
        
        sorted_items = sorted(dic.items())
        print(sorted_items)
        result = ''
        for ndx, val in sorted_items:
            result += str(val)
        return result
