class Solution {
public:
    int rangeSum(vector<int>& nums, int n, int left, int right) {

        multiset<int> s;
        const int MOD = static_cast<long long>(std::pow(10, 9)) + 7;

        for(int i=0; i<n; i++)
        {
            int sum = 0;
            for (int j=i; j<n; j++)
            {
                sum += nums[j];
                s.insert(sum);
            }
        }
        
        int sol = 0;
        auto it = s.begin();
        
        for(int i=0; i<s.size(); i++) 
        {
            if (i >= left-1 && i < right)
            {
                sol += *it;
                sol %= MOD;
            }
            it ++;
        }

        return sol % MOD;
    }
};