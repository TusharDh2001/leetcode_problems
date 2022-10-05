class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
      
      
      
      
      #another answer using hashmap
     '''
     
     
     
     class Solution:
 def containsDuplicate(self, nums: List[int]) -> bool:
   hashmap = dict()
 
   for i in range(len(nums)):
   if nums[i] in hashmap.keys():
     return True
   else:
     hashmap[nums[i]] = i
 
   return False
     '''
