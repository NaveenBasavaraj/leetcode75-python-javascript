class Hashing:
    def twoSum(self, nums, target):
        numIndexMap = {}
        
        for i, num in enumerate(nums):
            diff = abs(target-num)
            if diff in numIndexMap:
                return (numIndexMap[diff], i)
            numIndexMap[num] = i
        return -1
    
if __name__ == "__main__":
    res = Hashing()
    print(res.twoSum([2,3,4,5], 5))