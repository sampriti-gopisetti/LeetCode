class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        hashmap = {}

        def dfs(cur):
            if cur in hashmap:
                return hashmap[cur]
            copy = Node(cur.val)
            hashmap[cur] = copy
            for nei in cur.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None
