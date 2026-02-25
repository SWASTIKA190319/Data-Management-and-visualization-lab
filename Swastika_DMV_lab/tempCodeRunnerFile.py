import networkx as nx
import matplotlib.pyplot as plt

def create_complete_graph():
    while True:
        try:
            n = int(input("Enter number of vertices (must be > 3): "))
            if n > 3:
                break
            else:
                print("Vertices must be greater than 3. Try again.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Create a complete graph Kn
    G = nx.complete_graph(n)

    print(f"\nComplete Graph K{n} created.")
    print(f"Nodes: {G.nodes()}")
    print(f"Edges: {G.edges()}")

    # Visualize the graph
    plt.figure(figsize=(8, 6))
    nx.draw_circular(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=1000)
    plt.title(f"Complete Graph K{n}")
    plt.show()

if __name__ == "__main__":
    create_complete_graph()

