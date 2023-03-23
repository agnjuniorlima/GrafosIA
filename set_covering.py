from itertools import chain, combinations

def set_cover(universe, subsets):
    # Returns the minimum number of subsets required to cover the universe
    elements = set(elem for subset in subsets for elem in subset)
    if elements != universe:
        return None
    covering = []
    subsets = list(subsets)
    while subsets:
        subset = subsets.pop()
        covering.append(subset)
        subsets = [s for s in subsets if not s.issubset(subset)]
    return covering

universe = set(range(1, 11))
subsets = [set([0, 1, 2]), set([1, 3]), set([4, 3]),set([5]), set([5])]
print(set_cover(universe, subsets))