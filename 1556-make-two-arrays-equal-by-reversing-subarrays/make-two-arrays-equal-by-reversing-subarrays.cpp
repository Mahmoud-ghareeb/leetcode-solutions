class Solution {
public:
    bool canBeEqual(vector<int>& target, vector<int>& arr) {

        map<int, int> m;
        for(auto &i: arr)
        {
            m[i]++;
        }
            

        for(auto &i: target)
        {
            if (m.find(i) == m.end())
                return false;
            if (m[i] == 0)
                return false;

            m[i] -= 1; 
        }
            

        return true;
        
    }
};