class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, vertex1, vertex2):
        # Add edges in both directions since it's an undirected graph
        if vertex1 in self.graph_dict and vertex2 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
            self.graph_dict[vertex2].append(vertex1)

    def display_graph(self):
        for vertex, neighbors in self.graph_dict.items():
            print(f"{vertex}: {neighbors}")


if __name__ == '__main__':
    try:
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

        # Display the graph
        print("Graph Representation:")
        my_graph.display_graph()

    except Exception as e:
        print(f"Error: {e}. Please enter valid input.")
