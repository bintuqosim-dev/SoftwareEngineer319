// CPP program for min rotation to unlock
#include <bits/stdc++.h>
using namespace std;

int minRotation(int input, int unlock_code)
{
    int rotation = 0;
    int input_digit, code_digit;

   
    while (input || unlock_code) {
  
    
        input_digit = input % 10;
        code_digit = unlock_code % 10;

      
        rotation += min(abs(input_digit - code_digit), 
                   10 - abs(input_digit - code_digit));

     
        input /= 10;
        unlock_code /= 10;
    }

    return rotation;
}
 
 
int main()
{
    int input = 28756;
    int unlock_code = 98234;
    cout << "Minimum Rotation = "
        << minRotation(input, unlock_code);
    return 0;
}

