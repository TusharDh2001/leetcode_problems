class Solution {
public:
    bool isPalindrome(int x) {
        int n, num=x, digit, rev = 0;
     n = num;
     do
     {
         digit = num % 10;
         rev = (rev * 10) + digit;
         num = num / 10;
     } while (num != 0);
     if (n == rev)
         return true;
     else
         return false;

    return 0;
}
};


