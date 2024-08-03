class Solution {
public:
    bool canBeEqual(vector<int>& target, vector<int>& arr) {

        map<int, int> m;
        for(auto &i: arr)
        {
            if (m.find(i) == m.end())
            {
                m.insert({i, 1});
            }
            else
            {
                int temp = m[i];
                m[i] = temp+1;
            }
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