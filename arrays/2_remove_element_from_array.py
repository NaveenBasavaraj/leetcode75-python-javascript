def remove_element(nums, val):
    '''
    Given an integer array nums and an integer val, 
    remove all occurrences of val in nums in-place. 
    The order of the elements may be changed. 
    Then return the number of elements in nums which are not equal to val.
    '''
    l = 0
    for r in range(1, len(nums)):
        if nums[r] != val:
            nums[l] = nums[r]
            l += 1
        return l