from data_loader import load_edges, load_matching
from alignment_score import compute_alignment_score
from graph_matching import generate_initial_matching, optimize_matching
from graph_matching import greedy_matching

def main():
    # Load edges
    male_edges = load_edges('data/male_connectome_graph.csv.gz')
    female_edges = load_edges('data/female_connectome_graph.csv.gz')

    # Get node lists
    male_nodes = set([u for u, v in male_edges.keys()] + [v for u, v in male_edges.keys()])
    female_nodes = set([u for u, v in female_edges.keys()] + [v for u, v in female_edges.keys()])

    # Ensure the node lists are of the same size
    assert len(male_nodes) == len(female_nodes), "Node lists are not of the same size."

    # Generate initial matching
    initial_matching = generate_initial_matching(list(male_nodes), list(female_nodes))

    # Optimize matching
    optimized_matching = optimize_matching(male_edges, female_edges, initial_matching)

    # Compute alignment score
    alignment_score = compute_alignment_score(male_edges, female_edges, optimized_matching)
    print(f"Alignment Score: {alignment_score}")

if __name__ == "__main__":
    main()

def main():
    # Load edges
    male_edges = load_edges('data/male_connectome_graph.csv.gz')
    female_edges = load_edges('data/female_connectome_graph.csv.gz')

    # Generate matching using greedy algorithm
    matching = greedy_matching(male_edges, female_edges)

    # Compute alignment score
    alignment_score = compute_alignment_score(male_edges, female_edges, matching)
    print(f"Alignment Score: {alignment_score}")

