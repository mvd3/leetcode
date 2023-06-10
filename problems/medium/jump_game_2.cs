public class Solution {
    public int Jump(int[] nums) {
        if (nums.Length == 1)
            return 0;
        if (nums[0] >= nums.Length)
            return 1;

        int r = 0; // Number of steps
        int f = -1; // Farthest element in array
        int t = 0; // Target element

        for (int i = 0; i < nums.Length - 1; ++i) {
            f = nums[i] + i > f ? nums[i] + i : f;
            if (i == t) {
                ++r;
                t = f;
            }
        }
        return r;
    }
}