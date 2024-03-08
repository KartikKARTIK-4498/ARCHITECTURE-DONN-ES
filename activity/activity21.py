class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph_dict and vertex2 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
            self.graph_dict[vertex2].append(vertex1)

    def dfs(self, start_vertex, visited=None):
        if visited is None:
            visited = set()

        visited.add(start_vertex)
        print(start_vertex, end=" ")

        for neighbor in self.graph_dict[start_vertex]:
            if neighbor not in visited:
                self.dfs(neighbor, visited)


if __name__ == '__main__':
    try:
        # Create a graph
        my_graph = Graph()

        # Add vertices
        my_graph.add_vertex("A")
        my_graph.add_vertex("B")
        my_graph.add_vertex("C")
        my_graph.add_vertex("D")

        # Add edges
        my_graph.add_edge("A", "B")
        my_graph.add_edge("B", "C")
        my_graph.add_edge("C", "D")
        my_graph.add_edge("D", "A")

        # Perform DFS starting from vertex "A"
        print("Depth-First Traversal:")
        my_graph.dfs("A")

    except Exception as e:
        print(f"Error: {e}. Please enter valid input.")
