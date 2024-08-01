class Solution {
public:
    int countSeniors(vector<string>& details) {

        int sol = 0;
        for (auto i: details)
        {
            if (std::stoi(i.substr(11,2)) > 60)
            {
                sol ++;
            }
        }
        return sol;
    }
};