#include <iostream>
using namespace std; 

int main()
{
    int a = 0, b = 0;
    cin >> a >> b;
    int c = a-b, d = a+b; 
   
    if (c >= 0)
    {
        if (d % 2 == 0) cout << "[message] c >= 0 && d div by 2"
                      << "\n";
        else cout << "[message] c >= 0 && d not div by 2"
                      << "\n";

        if (d % 3 == 0) cout << "[message] c >= 0 && d div by 3"
                      << "\n";
        else cout << "[message] c >= 0 && d not div by 3"
                      << "\n";

        if (d % 4 == 0) cout << "[message] c >= 0 && d div by 4"
                      << "\n";
        else cout << "[message] c >= 0 && d not div by 4"
                      << "\n"; 

        if (d % 5 == 0) cout << "[message] c >= 0 && d div by 5"
                      << "\n";
        else cout << "[message] c >= 0 && d not div by 5"
                      << "\n";
        
        if (d % 6 == 0) cout << "[message] c >= 0 && d div by 6"
                      << "\n";
        else cout << "[message] c >= 0 && d not div by 6"
                      << "\n";
        
        if (d % 7 == 0) cout << "[message] c >= 0 && d div by 7"
                      << "\n";
        else cout << "[message] c >= 0 && d not div by 7"
                      << "\n";
        if (d % 8 == 0) cout << "[message] c >= 0 && d div by 8"
                      << "\n";
        else cout << "[message] c >= 0 && d not div by 8"
                      << "\n";

        if (d % 9 == 0) cout << "[message] c >= 0 && d div by 9"
                      << "\n";
        else cout << "[message] c >= 0 && d not div by 9"
                      << "\n";

        if (d % 10 == 0) cout << "[message] c >= 0 && d div by 10"
                      << "\n";
        else cout << "[message] c >= 0 && d not div by 10"
                      << "\n";

        if (d % 11 == 0) cout << "[message] c >= 0 && d div by 11"
                      << "\n";
        else cout << "[message] c >= 0 && d not div by 11"
                      << "\n";
    }
    else
    {
         if (d % 2 == 0) cout << "[message] c < 0 && d div by 2"
                      << "\n";
        else cout << "[message] c < 0 && d not div by 2"
                      << "\n";

        if (d % 3 == 0) cout << "[message] c < 0 && d div by 3"
                      << "\n";
        else cout << "[message] c < 0 && d not div by 3"
                      << "\n";

        if (d % 4 == 0) cout << "[message] c < 0 && d div by 4"
                      << "\n";
        else cout << "[message] c < 0 && d not div by 4"
                      << "\n";
        
        if (d % 5 == 0) cout << "[message] c < 0 && d div by 5"
                      << "\n";
        else cout << "[message] c < 0 && d not div by 5"
                      << "\n";
        
        if (d % 6 == 0) cout << "[message] c < 0 && d div by 6"
                      << "\n";
        else cout << "[message] c < 0 && d not div by 6"
                      << "\n";
        
        if (d % 7 == 0) cout << "[message] c < 0 && d div by 7"
                      << "\n";
        else cout << "[message] c < 0 && d not div by 7"
                      << "\n";
        if (d % 8 == 0) cout << "[message] c < 0 && d div by 8"
                      << "\n";
        else cout << "[message] c < 0 && d not div by 8"
                      << "\n";

        if (d % 9 == 0) cout << "[message] c < 0 && d div by 9"
                      << "\n";
        else cout << "[message] c < 0 && d not div by 9"
                      << "\n";

        if (d % 10 == 0) cout << "[message] c < 0 && d div by 10"
                      << "\n";
        else cout << "[message] c < 0 && d not div by 10"
                      << "\n";

        if (d % 11 == 0) cout << "[message] c < 0 && d div by 11"
                      << "\n";
        else cout << "[message] c < 0 && d not div by 11"
                      << "\n";
    }

    if (a >= 0)
    {
        if (b >= 0)
        {
            std::cout << "[message] a >= 0 && b >= 0"
                      << "\n";
        }
        else
        {
            std::cout << "[message] b < 0 && a >= 0."
                      << "\n";
        }
    }
    else
    {
        if (b >= 0)
        {
            std::cout << "[message] a < 0 && b >= 0"
                      << "\n";
        }
        else
        {
            std::cout << "[message] b < 0 && a < 0."
                      << "\n";
        }
    }
    return 0;
}