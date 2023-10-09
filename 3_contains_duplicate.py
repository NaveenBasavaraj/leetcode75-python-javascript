class ContainsDuplicate:

  def findDuplicatesSet(self, nums):
    hashSet = set()
    duplicates = set()
    for n in nums:
      if n in hashSet:
        duplicates.add(n)
      else:
        hashSet.add(n)
    return duplicates

  def findUniqueSet(self, nums):
    hashSet = set()
    duplicates = set()
    for n in nums:
      if n in hashSet:
        duplicates.add(n)
      else:
        hashSet.add(n)
    return duplicates ^ hashSet

  def findUniqueNumber(self, nums):
    res = 1
    for n in nums:
      res ^= n
    return res


res = ContainsDuplicate().findDuplicatesSet([1, 1, 3, 2, 4, 4, 5])

print(res)

uniques = ContainsDuplicate().findUniqueSet([1, 1, 3, 2, 4, 4, 5])

print(uniques)

unique = ContainsDuplicate().findUniqueNumber([1, 1, 3, 3, 2, 2, 4, 4, 5])

print(unique)
