def compute_alignment_score(male_edges, female_edges, matching):
    alignment = 0
    for (u, v), weight in male_edges.items():
        mapped_u = matching.get(u)
        mapped_v = matching.get(v)
        if mapped_u and mapped_v:
            female_weight = female_edges.get((mapped_u, mapped_v), 0)
            alignment += min(weight, female_weight)
    return alignment
