# https://leetcode.com/problems/product-of-array-except-self/description/

# brutforce - O(n2) with two loops when i != j do product
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        result = [0] * n
        for i in range(n):
            # to set the product equals to 1 for every begining of the i
            product = 1
            for j in range(n):
                if i!=j:
                    product *= nums[j]
            print(product)
            result[i] = product
        return result
    

solution = Solution()
print(solution.productExceptSelf([1,2,3,4]))


# class Solution:
#     def productExceptSelf(self, nums: list[int]) -> list[int]:
#         n = len(nums)
#         result = [0] * n

#         running_product = 1
#         result[0] = 1
#         # left side running product
#         for i in range(1,n):
#             running_product = running_product * nums[i - 1]
#             result[i] = running_product

#         running_product = 1
#         for i in range(n-2, -1, -1):
#             running_product = running_product * nums[i + 1]
#             result[i] = result[i] * running_product
        
#         return result
    
# solution = Solution()
# print(solution.productExceptSelf([1,2,3,4]))