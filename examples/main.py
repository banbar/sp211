# main.py
import sys
from pathlib import Path
import geopandas as gpd

# Add the project root to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from sp211 import graph, dijkstra


# Path to production data
DATA_DIR = Path(__file__).parent.parent / "data" / "production"

graph = graph.Graph()
graph.load_nodes(DATA_DIR / "nodes_ilceler.csv")
graph.load_edges(DATA_DIR / "edges_ilceler.csv")

gdf = gpd.read_file(DATA_DIR / "DT_ilceler.gpkg", layer="edges")

start_node = '265'
end_node = '302'
costs, previous = dijkstra.shortest_path(graph, start_node)
print(costs)
graph.export_shortest_path(previous, start_node, end_node, gdf)
