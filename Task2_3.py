def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)     # Record each value of new_list and value at the end of the loop body.
                                        # First loop: new_list is [5], value is 4,
                                        # Second loop: new_list is [5, 10], value is 9,
                                         #Third loop: new_list is [5, 10, 3], value is 2,
                                        # Fourth loop: new_list is [5, 10, 3, 2], value is 1

    return new_list

result = increment_all([4, 9, 2, 1])