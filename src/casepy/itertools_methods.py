from .combination_generator import CombinationGenerator


def combinations(iterable, r):
    pool = tuple(iterable)

    tempGenerator = CombinationGenerator()
    tempGenerator.set_parameters(r, pool)
    return tempGenerator.all_case()
