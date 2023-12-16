#include<bits/stdc++.h>
using namespace std;

// Variables definition

void print_solution()
{
    // Print best solution
}

void print_best_solution()
{
    // Print found solution
}

template <class T>
T evaluate()
{
    // Return score of current solution
}

template <class T>
bool check(T v, int k)  // Check if value v in index k violate any rule
{
    return true;
}

template <class T>
void Try(int k)  // Try value for index k
{
    T A[];  // Selectable value for index k
    for (T v: A)
    {
        if (check(v, k))
        {
            // Update value v for index k

            if (k == 2*n)  // Last index to check
            {
                // Save current solution if it's best solution
                // Update best
            }
            else  // Not last index
            {
                if (evaluate() < best_score)  // Remove branch that cannot be best
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
    branch_and_bound(1);
    print_best_solution();
}

int main()
{
    input();
    init();
    solve();
    return 0;
}
