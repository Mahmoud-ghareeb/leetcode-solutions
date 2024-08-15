class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {

        map<int, int> wallet {
            {5, 0},
            {10, 0},
            {20, 0}
        };
        for(int &i: bills)
        {

            // for(auto &j: wallet)
            //     cout << j.first << " -> " << j.second << " ";
            // cout << "\n";

            int change = i - 5;

            if (change == 5)
            {
                if (wallet[5] <= 0)
                    return false;
                else 
                {
                    wallet[5] -= 1;
                }
            }
            else if (change == 15)
            {
                if (wallet[10] <= 0 and wallet[5] <= 2)
                    return false;
                
                if (wallet[10] > 0)
                {
                    if (wallet[5] >= 1)
                    {
                        wallet[10] -= 1;
                        wallet[5] -= 1;
                    }
                    else
                    {
                        return false;
                    }
                }
                else if (wallet[5] >= 3)
                    wallet[5] -= 3;
                else
                    return false;
            }

            wallet[i] ++;
        }


        return true;
    }
};