#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int minCoins(vector<int>& coins, int amount) {
    sort(coins.rbegin(), coins.rend()); 
    int count = 0;

    for (int coin : coins) {
        if (amount == 0) break;
        if (coin <= amount) {
            count += amount / coin;    
            amount %= coin;            
        }
    }

    return (amount == 0) ? count : -1; 
}

int main() {
    vector<int> coins = {1, 5, 10, 25}; 
    int amount;
    
    cout << "Enter the amount to be paid: ";
    cin >> amount;

    int result = minCoins(coins, amount);
    if (result != -1) {
        cout << "Minimum number of coins: " << result << endl;
    } else {
        cout << "It is not possible to pay this amount with these coins." << endl;
    }

    return 0;
}
