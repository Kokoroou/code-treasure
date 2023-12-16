#include<bits/stdc++.h>
using namespace std;

int main()
{
    // Open files to read and write data
    fstream input("input_file.txt");
    fstream output;
    output.open("output_file.txt", ios::out);

    // Working with file
    int a;
    input >> a;
    output << a;

    // Close files
    input.close();
    output.close();

    return 0;
}
