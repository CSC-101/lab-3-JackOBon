def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])     # Record each value of new_list and idx at the end of the loop body.    ([4], 0), ([4,9],1), ([4,9,2],2), ([4,9,2,1], 3)
    return new_list                    # How does this loop differ from that above? This loop differs from the tally loops because tally loops over values and copy over a range of indices and accesses elements of the list through nums[idx]

result = copy([4, 9, 2, 1])