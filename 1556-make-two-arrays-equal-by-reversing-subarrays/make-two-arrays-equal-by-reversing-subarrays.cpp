class Solution {
public:
    bool canBeEqual(vector<int>& target, vector<int>& arr) {

        multiset<int> s1;
        multiset<int> s2;

        for(auto &i: arr)
            s1.insert(i);

        for(auto &i: target)
            s2.insert(i);

        return s1 == s2;
        
    }
};