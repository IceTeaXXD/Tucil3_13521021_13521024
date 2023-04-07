def list_to_adjacent_pairs(lst) -> list:
    return [(lst[i], lst[i+1]) for i in range(len(lst)-1)]