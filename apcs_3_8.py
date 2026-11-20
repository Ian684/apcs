def multiply_left_right(numbers, target):
    """Return the indices of two numbers that multiply to target, or None."""
    seen = {}
    for index, number in enumerate(numbers):
        if number == 0:
            if target == 0:
                if 0 in seen:
                    return seen[0], index
            seen.setdefault(number, index)
            continue
        if target % number == 0:
            needed = target // number
            if needed in seen:
                return seen[needed], index
        seen.setdefault(number, index)
    return None
