class Solution {
public:
    int minimumPushes(string word) {

        map<char, int> m;

        for(auto &i: word)
            m[i]++;

        vector<pair<char, int>> v {m.begin(), m.end()};

        sort(v.begin(), v.end(), [](const auto& a, const auto& b) {
            return a.second > b.second;
         });
        
        int sol = 0;
        int mul = 0;
        int i = 0;
        for(auto &r : v)
        {
            if (i % 8 == 0)
                ++mul;

            sol += (mul * r.second);
            ++i;
        }
        
        return sol;
    }
};