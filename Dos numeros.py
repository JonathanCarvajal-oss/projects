#Dentro de una cantidad de numeros tomar 2 y sumarlos para que de la target que es On elevado al cuadrado
##   def twoSum(self, nums: list[int], target: int) -> list[int]:
  #      hashmap = {}
   #     for i in range(len(nums)):
    #        complement = target - nums[i]
     #       if complement in hashmap:
      #          return [i, hashmap[complement]]
       #     hashmap[nums[i]] = i
            
#numero 2
#class Solution:
 #   def twoSum(self, nums: List[int], target: int) -> List[int]:
  #      hashmap = {}
   #     for i in range(len(nums)):
    #        hashmap[nums[i]] = i
     #   for i in range(len(nums)):
      #      complement = target - nums[i]
       #     if complement in hashmap and hashmap[complement] != i:
        #        return [i, hashmap[complement]]

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

n = 2*3+3**2
print(n)
