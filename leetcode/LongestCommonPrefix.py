class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        adict = {}
        
        if len(strs) == 1:
            return strs[0]
        selected = min(strs)
        
        for idxS in range(0, len(strs)):
            curr_string = strs[idxS]
            for idxC in range(len(curr_string)):
                if len(selected) <= idxC:
                    break
                if selected[idxC] == curr_string[idxC]:
                    continue
                else:
                    selected = selected[0:idxC]
                    break
            
                    
        return selected