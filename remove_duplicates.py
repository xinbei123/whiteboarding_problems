def deduped(items):
    """Return new list from items with duplicates removed."""

    result = [] 
    seen = set()

    for item in items:

        if item not in seen:

            result.append(item)
            seen.add(item)

    return result

    





print(deduped([1, 1, 1]))
#[1]

print(deduped([1, 2, 3]))
#[1, 2, 3]

print(deduped([])) # []
