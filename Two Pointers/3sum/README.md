Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

Big O Notation explanations:

1. **Sorting Complexity**: The sorting step is done using a sorting algorithm with a time complexity of O(n log n), where 'n' is the number of elements in the array. This sorting step happens only once at the beginning of the function.

2. **Outer Loop Complexity**: The outer loop iterates through each element of the sorted array. Since there are 'n' elements in the array, this loop contributes O(n) to the overall time complexity.

3. **Inner Loop Complexity**: The inner loop searches for pairs of elements that sum up to the negation of the current element. It continues as long as the left pointer `l` is less than the right pointer `r`. In the worst case, both pointers traverse the entire array (approximately 'n' iterations) before converging. Therefore, the inner loop contributes O(n) to the overall time complexity.

4. **While Loop within Inner Loop**: The innermost `while` loop is used to skip over duplicate elements. In the worst case, this loop can run for almost 'n' iterations because it could iterate over the remaining elements between `l` and `r` if they are all duplicates.

Putting it all together:

- Sorting: O(n log n)
- Outer Loop: O(n)
- Inner Loop: O(n)
- Innermost While Loop: O(n) in the worst case

The sorting step is a one-time cost, and the nested loops within the outer loop are the primary contributors to the time complexity. When you consider the outer loop and the two nested loops, the overall time complexity becomes:

O(n) (outer loop) * (O(n) (inner loop) + O(n) (innermost while loop))

Simplified: O(n^2)

In summary, the sorting step and the nested loops over the sorted array are responsible for the quadratic time complexity of O(n^2) in the `threeSum` function. This indicates that the function's execution time grows quadratically with the number of input elements.

The space complexity of the given `threeSum` function primarily depends on the extra space used for storing the result (`res`) and the variables used for loop control and temporary calculations. Let's break down the main components contributing to the space complexity:

1. **Result Space**: The `res` list stores all the triplets that sum up to zero. In the worst case, where there are numerous valid triplets, the space required for the `res` list can be proportional to the number of valid triplets. In terms of big O notation, this can be approximated as O(n^2), since in the worst case, there could be O(n^2) valid triplets.

2. **Loop Control Variables**: The loop control variables like `i`, `num`, `l`, and `r` do not grow with the input size but remain constant. Therefore, their space consumption is constant and can be disregarded when analyzing space complexity.

3. **Temporary Variables**: The temporary variables like `sum` are used for calculations and comparisons within loops. These variables have a constant space requirement that doesn't depend on the input size.

Putting it all together, the dominant factor in the space complexity is the space used for the `res` list, which can grow up to O(n^2) in the worst case. Therefore, the overall space complexity of the `threeSum` function can be approximated as O(n^2), where 'n' is the number of elements in the input list.