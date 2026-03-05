class Graph:
    """Directed graph using adjacency list (can be adapted to undirected)."""

    def __init__(self):
        self._graph = {}

    def add_edge(self, u, v):
        """Add directed edge u -> v."""
        if u not in self._graph:
            self._graph[u] = []
        self._graph[u].append(v)

    def bfs(self, start):
        """Breadth‑first search returning traversal order."""
        visited = set()
        queue = [start]
        result = []
        if start in self._graph:
            visited.add(start)
            while queue:
                node = queue.pop(0)
                result.append(node)
                for neighbor in self._graph.get(node, []):
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
        return result

    def dfs_recursive(self, start, visited=None):
        """DFS (recursive)."""
        if visited is None:
            visited = set()
        visited.add(start)
        result = [start]
        for neighbor in self._graph.get(start, []):
            if neighbor not in visited:
                result.extend(self.dfs_recursive(neighbor, visited))
        return result

    def dfs_iterative(self, start):
        """DFS (iterative using stack)."""
        visited = set()
        stack = [start]
        result = []
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                result.append(node)
                # Push neighbors in reverse order to mimic recursion order
                for neighbor in reversed(self._graph.get(node, [])):
                    if neighbor not in visited:
                        stack.append(neighbor)
        return result

if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'E')
    g.add_edge('D', 'E')

    print("BFS from A:", g.bfs('A'))
    print("DFS (recursive) from A:", g.dfs_recursive('A'))
    print("DFS (iterative) from A:", g.dfs_iterative('A'))
