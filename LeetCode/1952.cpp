//TC : O(prime_number)
//SC : O(prime_number)

class Solution {
private:
    
public:
    bool isThree(int n) {
        int prime_number[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};

        for (int i = 0; i<sizeof(prime_number)/sizeof(int); i++)
        {
            if (n == prime_number[i]*prime_number[i])
            {
                return true;
            }
        }
        return false;
    }
};