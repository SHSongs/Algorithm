//TC: O(N)
//TS: O(1)

using std::vector;

class Solution {
public:
    long long numberOfWeeks(vector<int>& milestones) {
        long long sum = 0;
        long long max = -999;
        int max_index = -1;
        
        for (auto& n : milestones)
        {
            sum += n;
            if (max < n)
            {
                max = n;
            }
        }
        
        if (sum - max + 1 >= max)
        {
            return sum;        
        }
        else
        {
            return (sum - max) * 2 + 1;
        }
    }
};