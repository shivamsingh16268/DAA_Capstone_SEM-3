
def merge_sort_parcels(parcels):
    """
    Sort parcels by priority (highest first).
    If priorities are equal, earlier deadlines come first.
    """

    if len(parcels) <= 1:
        return parcels

    mid = len(parcels) // 2

    left = merge_sort_parcels(parcels[:mid])
    right = merge_sort_parcels(parcels[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if (left[i]["priority"], -left[i]["deadline"]) >= (
            right[j]["priority"], -right[j]["deadline"]
        ):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result
