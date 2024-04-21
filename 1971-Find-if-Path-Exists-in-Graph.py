class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        hashMap = defaultdict(list)

        for s, d in edges:
            hashMap[s].append(d)
            hashMap[d].append(s)

        def dfs(node, visited):
            if node == destination:
                return True

            visited.add(node)

            for edge in hashMap[node]:
                if edge not in visited:
                    if dfs(edge, visited): return True

            return False


        visited = set()
        return dfs(source, visited)




        