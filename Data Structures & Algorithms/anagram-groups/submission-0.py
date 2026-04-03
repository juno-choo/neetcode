from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        parent = defaultdict(list)
        for i in range(len(strs)):
            child = [0]*26
            for c in strs[i]:
                child[ord(c) - ord("a")] += 1
            child = tuple(child)
            parent[child].append(strs[i])
        return list(parent.values())

               
                    

        # ["eat","tea","tan","ate","nat","bat"]
        #                                  i
        
        # # if len is the same, we check if the freq is the same
        # # 
        
        # { e:1, a:1, t:1 } : ["eat", "tea", "ate"]
        # { t:1, a:1, n:1 } : ["tan", "nat"]
        # { b:1, a:1, t:1 } : ["bat"]


        
