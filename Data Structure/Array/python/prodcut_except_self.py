class Solution:
    """Check whether a matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.

    Args:
        nums: an array nums of n integers where n > 1.

    Returns:
        an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

    Example:
        Input:  [1,2,3,4]
        Output: [24,12,8,6]


    Idea of solution:
        We can do the left product first and then right product to calcualte the product without itself.
        Using the exmaple above, the left product will be [1,1,2,6], right product will be [24,12,4,1].
        After that we can do left[i] * right[i], then we can have our final result.

    Time Complexity: O(n)
    Space Complexity: O(n) 
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        prod = 1
        for i in range(len(nums)-2, -1, -1):
            prod *= nums[i+1]
            res[i] = res[i] * prod
        return res
