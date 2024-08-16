class Solution {
public:
    int maxDistance(vector<vector<int>>& arrays) {

        int n = arrays[0].size();
        int min_min = arrays[0][0];
        int max_max = arrays[0][n-1];
        int max_dis = 0;

        for (auto i =1; i<arrays.size(); ++i)
        {
            n = arrays[i].size();
            max_dis = max(max_dis, max(abs(arrays[i][n-1] - min_min), abs(max_max - arrays[i][0])));
            min_min = min(min_min, arrays[i][0]);
            max_max = max(max_max, arrays[i][n-1]);
        }

        return max_dis;
        
    }
};