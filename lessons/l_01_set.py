def l_01_set():
    # set is unordered, unindexed, and does not allow duplicate values
    post_ids = {123, 123, 456, 789, 123}
    print(f"post_ids: {post_ids}")  # {123, 456, 789}

    # set can't contains mutable types like list or dict

    # methods
    # post_ids = {123, 123, 456, 789, 123}
    post_ids.add(101)
    print(f"post_ids after add: {post_ids}")  # {101, 123, 456, 789}

    # union
    # post_ids = {123, 123, 456, 789, 123}
    post_ids2 = {101, 456, 789}
    post_ids = post_ids.union(post_ids2)  # {101, 123, 456, 789}

    # remove
    # post_ids = {123, 123, 456, 789, 123}
    post_ids.remove(123)
    print(f"post_ids after remove: {post_ids}")  # {101, 456, 789}

    # difference
    # post_ids = {123, 123, 456, 789, 123}
    post_ids3 = {101, 456}
    difference = post_ids.difference(post_ids3)
    print(f"difference: {difference}")  # {789}

    # intersection
    # post_ids = {123, 123, 456, 789, 123}
    post_ids4 = {456, 789}
    intersection = post_ids.intersection(post_ids4)
    print(f"intersection: {intersection}")  # {456, 789}

    # discard
    # this will not raise an error if the element is not found
    # post_ids = {123, 123, 456, 789, 123}
    post_ids.discard(456)
    print(f"post_ids after discard: {post_ids}")  # {101, 789}

    # clear
    # post_ids = {123, 123, 456, 789, 123}
    post_ids.clear()
    print(f"post_ids after clear: {post_ids}")  # set()

    # copy
    # post_ids = {123, 123, 456, 789, 123}
    post_ids = {123, 456, 789}
    post_ids_copy = post_ids.copy()
    print(f"post_ids_copy: {post_ids_copy}")  # {123, 456, 789}

    # update
    # post_ids = {123, 123, 456, 789, 123}
    post_ids.update({101, 102})
    print(f"post_ids after update: {post_ids}")  # {101, 102, 123, 456, 789}
    
    # issuperset
    # post_ids = {123, 456, 789}
    post_ids5 = {123, 456}
    is_superset = post_ids.issuperset(post_ids5)
    print(f"post_ids is superset of post_ids5: {is_superset}")  # True

    # issubset
    # post_ids = {123, 456, 789}
    post_ids6 = {123, 456, 789, 101}
    is_subset = post_ids6.issubset(post_ids)
    print(f"post_ids6 is subset of post_ids: {is_subset}")  # False

    # pop
    # post_ids = {123, 456, 789}
    post_ids7 = {123, 456, 789}
    popped_item = post_ids7.pop()  # removes and returns an arbitrary element
    print(f"popped item: {popped_item}")  # could be any of the elements


