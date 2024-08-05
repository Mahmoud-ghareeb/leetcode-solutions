class Solution {
public:
    string kthDistinct(vector<string>& arr, int k) {

        map<string, int> m;

        for (auto &i : arr)
            m[i]++;

        int x = 0;
        for (auto &i : arr)
        {
            if (m[i] == 1 && ++x && x == k)
                return i;
        }

        return "";
        
    }
};