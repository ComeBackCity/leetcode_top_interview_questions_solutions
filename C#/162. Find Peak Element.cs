public class Solution {
    public int FindPeakElement(int[] nums) {
        int l = 0, r = nums.Length - 1;
        while (l<r){
            int mid1 = (l+r) / 2;
            int mid2 = mid1+1;
            if(nums[mid1] < nums[mid2]){
                l = mid2;
            }
            else {
                r = mid1;
            }
        }
        
        return l;
    }
}