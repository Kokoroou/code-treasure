#include<bits/stdc++.h>
using namespace std;
#define Template template <class T>
#define N 1000  // Limit of test cases

// Variables definition
Template T x[N];  // Store solution
int n;  // Last index

void print_solution()
{
    // Print found solution
}

Template bool check(T v, int k)  // Check if value v in index k violate any rule
{
    return true;
}

Template void Try(int k)  // Try value for index k
{
    T A[];  // Selectable value for index k
    for (T v: A)
    {
        if (check(v, k))
        {
            // Update value v for index k

            if (k == n)  // Last index to check
            {
                // Save or print all values of all indexes
                print_solution();
            }
            else  // Not last index
            {
                Try(k+1);
            }

            // Turn back to state before update value v for index k

        }
    }

}

void input()
{
    // Get value from input
}

void init()
{
    // Initialize value for global variables
}

void solve()
{
    // Solve problem
    Try(0);
}


int main()
{
    input();
    init();
    solve();
    return 0;
}
