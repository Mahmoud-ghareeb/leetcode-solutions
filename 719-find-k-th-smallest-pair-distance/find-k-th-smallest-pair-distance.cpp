class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        int n = nums.size();

        int maxElement = *max_element(nums.begin(), nums.end());

        vector<int> distanceBucket(maxElement + 1, 0);

        for (int i = 0; i < n; ++i)
            for (int j = i + 1; j < n; ++j)
                ++distanceBucket[abs(nums[i] - nums[j])];
            
        for (int dist = 0; dist <= maxElement; ++dist) {
            k -= distanceBucket[dist];
            if (k <= 0) {
                return dist;
            }
        }
        return -1;
    }
};