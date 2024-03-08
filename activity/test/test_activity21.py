from activity.activity21 import Graph

def test_dfs(capsys):
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_edge('A', 'B')
    graph.add_edge('B', 'C')
    graph.add_edge('C', 'D')

    graph.dfs('A')

    captured = capsys.readouterr()
    expected_output = "A B C D "
    assert captured.out == expected_output

def test_dfs_with_disconnected_graph(capsys):
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_edge('A', 'B')
    graph.add_edge('C', 'D')


    graph.dfs('A')

    captured = capsys.readouterr()
    expected_output = "A B "
    assert captured.out == expected_output
