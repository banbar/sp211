import pytest
from pathlib import Path
from sp211.graph import Graph

@pytest.fixture
def small_test_graph():
    data_dir = Path(__file__).resolve().parent.parent / "data" / "test"
    g = Graph()
    g.load_nodes(data_dir / "nodes.csv")
    g.load_edges(data_dir / "edges.csv")
    return g
