class Solution {
public:
    int climbStairs(int n) {
        if (n <= 2){
            return n;
        }
        int x = 1, y = 2, sol = 0;

        for (int i=3; i<n+1; i++){
            sol  = x + y;
            x = y, y = sol;
        }

        return sol;
        
    }
};