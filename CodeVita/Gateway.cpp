#include <iostream>
#include <vector>
#include <string>

using namespace std;

bool isPalindrome(const string& s) {
    int i = 0, j = s.length() - 1;
    while (i < j) {
        if (s[i] != s[j]) {
            return false;
        }
        i++;
        j--;
    }
    return true;
}

int main() {
    vector<string> names;
    string name;
    
    // Input names
    while (cin >> name) {
        names.push_back(name);
    }

    int N;
    cin >> N;

    // First elimination round based on palindrome criteria
    for (int i = 0; i < names.size(); ++i) {
        string S;
        for (int j = i; j < names.size(); ++j) {
            S += names[j][0];

            if (isPalindrome(S)) {
                names.erase(names.begin() + j);
                --j; // Adjust index after erasing an element
            }
        }
    }

    // Second elimination round based on interval N
    int index = 0;
    while (names.size() > 1) {
        index = (index + N - 1) % names.size();
        names.erase(names.begin() + index);
    }

    // Output the winner
    cout << names[0] << endl;

    return 0;
}
