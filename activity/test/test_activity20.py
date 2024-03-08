from activity.activity20 import Graph

def test_add_vertex():
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')

    assert 'A' in graph.graph_dict
    assert 'B' in graph.graph_dict
    assert 'C' not in graph.graph_dict

def test_add_edge():
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')

    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')

    assert 'B' in graph.graph_dict['A']
    assert 'A' in graph.graph_dict['B']
    assert 'C' in graph.graph_dict['B']
    assert 'B' in graph.graph_dict['C']
    assert 'A' not in graph.graph_dict['C']

def test_display_graph(capsys):
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_edge('A', 'B')

    graph.display_graph()

    captured = capsys.readouterr()
    expected_output = "A: ['B']\nB: ['A']\n"
    assert captured.out == expected_output
