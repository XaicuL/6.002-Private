###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

# ================================
# Part B: Golden Eggs
# ================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo={}):
    if target_weight == 0:
        return 0

    if target_weight in memo:
        return memo[target_weight]

    min_eggs = target_weight

    for egg in egg_weights:
        if egg <= target_weight:
            num_eggs = 1 + dp_make_weight(egg_weights, target_weight - egg, memo)
            if num_eggs < min_eggs:
                min_eggs = num_eggs

    memo[target_weight] = min_eggs
    return min_eggs


if __name__ == '__main__':
    egg_weights = (1, 5, 10, 25)
    n = 99
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()
