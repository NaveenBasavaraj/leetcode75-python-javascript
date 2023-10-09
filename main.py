class TwoSum:
  # value is made as key
  # and key is made as index
  def with_enumerate(self, nums, target, ret_val=False):
    hashMap = {}
    for i, val in enumerate(nums):
      diff = target - val
      if diff in hashMap:
        if ret_val:
          return (val, diff)
        return (i, hashMap[diff])
      else:
        # value is made as key
        # and key is made as index
        hashMap[val] = i
    return

  def without_enumerate(self, nums, target, ret_val=False):
    hashMap = {}
    for i in range(len(nums)):
      diff = target - nums[i]
      if diff in hashMap:
        if ret_val:
          return (nums[i], diff)
        return (i, hashMap[diff])
      else:
        hashMap[nums[i]] = i
    return


result = TwoSum().with_enumerate(nums=[1, 2, 3, 4, 5], target=8)

print(result)

result = TwoSum().without_enumerate(nums=[1, 2, 3, 4, 5], target=8)

print(result)

result = TwoSum().with_enumerate(nums=[1, 2, 3, 4, 5], target=8, ret_val=True)

print(result)

result = TwoSum().without_enumerate(nums=[1, 2, 3, 4, 5],
                                    target=8,
                                    ret_val=True)

print(result)
