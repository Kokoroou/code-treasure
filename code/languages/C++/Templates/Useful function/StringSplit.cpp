#include <bits/stdc++.h>
using namespace std;

//Parsing a string into a vector of strings by delimiter
vector<string> split(string s, string delimiter)
{
    vector<string> tokens;
    size_t pos;

    while ((pos = s.find(delimiter)) != string::npos)
    {
        tokens.push_back(s.substr(0, pos));
        s.erase(0, pos + delimiter.length());
    }
    tokens.push_back(s);

    return tokens;
}

int main()
{
    int n;
    cin >> n;

    string s;

    // Clear input
    string dummy;
    getline(cin, dummy);

    // Get line from input to string s
    getline(cin, s);

    return 0;
}
