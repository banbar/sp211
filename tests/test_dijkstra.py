from sp211.dijkstra import shortest_path

def test_shortest_path_cost_from_A(small_test_graph):
    cost, prev = shortest_path(small_test_graph, 'A')
    
    assert cost['G'] == 17
    
    # Test direct neighbor costs
    assert cost['B'] == 8
    assert cost['E'] == 6
    assert cost['F'] == 12
    assert prev['F'] == 'B'
    assert prev['G'] == 'C'

def test_shortest_path_trace_from_D(small_test_graph):
    cost, prev = shortest_path(small_test_graph, 'D')
    
    # D → E → C → G = 3 + 6 + 5 = 14
    assert cost['G'] == 14
    assert prev['A'] == 'D'
    assert prev['B'] == 'D'  # D → B is a valid path
    assert prev['G'] == 'C'
    assert prev['C'] == 'E'
    assert cost['A'] == 3
