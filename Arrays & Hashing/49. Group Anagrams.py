class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        main_a={}  
        return_a=[] 
        for s in strs:
            string="".join(sorted(s))
            if string not in main_a:
                main_a[string]= [s]
            else:
                main_a[string].append(s)
        for key in main_a:
            return_a.append(main_a[key])
        return return_a