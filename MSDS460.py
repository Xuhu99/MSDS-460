import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Define the graph edges with weights (miles, costs, or minutes)
edges = [
    ('Origin', 'A', 40), ('Origin', 'B', 60), ('Origin', 'C', 50),
    ('A', 'B', 10), ('A', 'D', 70),
    ('B', 'C', 20), ('B', 'E', 40),
    ('C', 'D', 50), ('C', 'E', 40),
    ('D', 'E', 10), ('D', 'Destination', 60),
    ('E', 'Destination', 80)
]

# Create a directed graph
G = nx.DiGraph()
G.add_weighted_edges_from(edges)

# UI Title
st.title("🚗 Shortest Path Finder (Dijkstra's Algorithm)")

# Let user choose start and end nodes
start_node = st.selectbox("Select Start Node", options=G.nodes, index=0)
end_node = st.selectbox("Select End Node", options=G.nodes, index=len(G.nodes) - 1)

# Draw graph
def draw_graph(graph, path=None):
    pos = nx.spring_layout(graph, seed=42)
    plt.figure(figsize=(12, 8))
    edge_colors = ['red' if path and (u, v) in zip(path, path[1:]) else 'gray' for u, v in graph.edges()]
    nx.draw(graph, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=10, edge_color=edge_colors, width=2)
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    st.pyplot(plt)

# On button click, calculate path
if st.button("Find Shortest Path"):
    try:
        path = nx.dijkstra_path(G, start_node, end_node)
        total = nx.dijkstra_path_length(G, start_node, end_node)
        st.success(f"Shortest Path: {' → '.join(path)}")
        st.info(f"Total Distance: {total} miles")
        st.info(f"Cost: ${total}")
        st.info(f"Time: {total} minutes")
        draw_graph(G, path)
    except nx.NetworkXNoPath:
        st.error("No path found between selected nodes.")
else:
    draw_graph(G)
