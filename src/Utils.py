import math

def list_to_adjacent_pairs(lst) -> list:
    return [(lst[i], lst[i+1]) for i in range(len(lst)-1)]

def euclidean_distance(p1, p2) -> float:
    return ((((p1[1] - p2[1])**2 + (p1[0] - p2[0])**2)**0.5) *111.322)