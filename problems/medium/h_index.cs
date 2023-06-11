public class Solution {
    public int HIndex(int[] citations) {
        Array.Sort(citations);
        int r = citations.Length;
        for (int i = 0; i < citations.Length; ++i)
            if (citations[i] < r)
                --r;
        return r;
    }
}