def create_bst_from_sorted(values):
    if not values:
        return None

    mid = len(values) // 2
    root = BinarySearchTree(values[mid])
    root.set_left(create_bst_from_sorted(values[:mid]))
    root.set_right(create_bst_from_sorted(values[mid + 1:]))

    return root
