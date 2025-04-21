import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Define the graph edges with weights (in miles, dollars, or minutes)
edges = [
    ('Origin', 'A', 40), ('Origin', 'B', 60), ('Origin', 'C', 50),
    ('A', 'B', 10), ('A', 'D', 70),
    ('B', 'C', 20), ('B', 'E', 40),
    ('C', 'D', 50), ('C', 'E', 40),
    ('D', 'E', 10), ('D', 'Destination', 60),
    ('E', 'Destination', 80)
]

# Step 2: Create a directed graph
G = nx.DiGraph()
G.add_weighted_edges_from(edges)

# Step 3: Display the graph visually
def draw_graph(graph):
    pos = nx.spring_layout(graph, seed=42)
    plt.figure(figsize=(12, 8))
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.title("Town Network with Distances")
    plt.show()

# Step 4: Compute the shortest path
def find_shortest_path(graph, start, end):
    try:
        path = nx.dijkstra_path(graph, start, end)
        length = nx.dijkstra_path_length(graph, start, end)
        return path, length
    except nx.NetworkXNoPath:
        return None, float('inf')

# MAIN EXECUTION
if __name__ == "__main__":
    draw_graph(G)

    start_node = 'Origin'
    end_node = 'Destination'

    path, total_distance = find_shortest_path(G, start_node, end_node)

    if path:
        print("Shortest path:", " → ".join(path))
        print("Total distance:", total_distance, "miles")
        print("Interpreted as cost: $", total_distance)
        print("Interpreted as time: ", total_distance, "minutes")
    else:
        print(f"No path found from {start_node} to {end_node}.")
