class ContainsDuplicate:
    def hasDuplicates(self, nums):
        hashSet = set()
        
        for num in nums:
            if num in hashSet:
                return True
            hashSet.add(num)
        return False

if __name__ == "__main__":
    result =  ContainsDuplicate()
    print(result.hasDuplicates([1,2,3,2]))
    print(result.hasDuplicates([1,2,3,4]))