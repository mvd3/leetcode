/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    var numbers = {}
    for (var i = 0; i < nums.length; i++) {
        if (numbers[target - nums[i]] != undefined)
            return [numbers[target - nums[i]], i];
        numbers[nums[i]] = i;
    }
};