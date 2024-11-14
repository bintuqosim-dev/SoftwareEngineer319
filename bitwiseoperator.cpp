#include <iostream>
using namespace std;

int main() {
    int a, b;

    // Taking input from the user
    cout << "Enter the first number (a): ";
    cin >> a;
    
    cout << "Enter the second number (b): ";
    cin >> b;

    cout << "\na = " << a << ", b = " << b << endl;

    // Bitwise AND
    cout << "a & b = " << (a & b) << " (Bitwise AND)" << endl;

    // Bitwise OR	
    cout << "a | b = " << (a | b) << " (Bitwise OR)" << endl;

    // Bitwise XOR
    cout << "a ^ b = " << (a ^ b) << " (Bitwise XOR)" << endl;

    // Bitwise NOT (only on a)
    cout << "~a = " << (~a) << " (Bitwise NOT of a)" << endl;
    cout << "~b = " << (~b) << " (Bitwise NOT of b)" << endl;

    // Left shift
    cout << "a << 1 = " << (a << 1) << " (Left shift a by 1)" << endl;
    cout << "b << 1 = " << (b << 1) << " (Left shift b by 1)" << endl;

    // Right shift
    cout << "a >> 1 = " << (a >> 1) << " (Right shift a by 1)" << endl;
    cout << "b >> 1 = " << (b >> 1) << " (Right shift b by 1)" << endl;

    return 0;
} 
