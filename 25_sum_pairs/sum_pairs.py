def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    answer = list()
    if nums[0] + nums[1] == goal:
        answer.append(nums[0])
        answer.append(nums[1])
    for num in nums:
        if nums.index(num) > 0 and len(answer) < 2:
            for index in range(nums.index(num),-1,-1):
                if num + nums[index] == goal:
                    answer.append(num)
                    answer.append(nums[index])

    return tuple(answer)
