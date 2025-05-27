def test_graph_node_count(small_test_graph):
    assert len(small_test_graph.nodes) > 0, "No nodes loaded"

def test_graph_edge_count(small_test_graph):
    assert len(small_test_graph.edges) == 13, "Expected 13 edges"

def test_node_existence(small_test_graph):
    assert small_test_graph.exists_node('A')
    assert not small_test_graph.exists_node('Z')
