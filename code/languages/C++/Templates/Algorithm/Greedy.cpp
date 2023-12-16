#include<bits/stdc++.h>
using namespace std;

// Variables definition
template <class T>
vector<T> C;  // Store candidates
vector<T> S;  // Store current solution

template <class T>
T select(vector<T> C)
{
    // Return best candidate from C
    return x;
}

template <class T>
void pop(vector<T> C, T x)
{
    // Pop candidate x from C
}

template <class T>
void add(vector<T> S, T x)
{
    // Add candidate x to S
}

template <class T>
bool is_solution(vector<T> S)
{
    // Check if current solution S is the solution for problem
}

template <class T>
bool check(vector<T> S, T x)  // Check if add x to S does not violate any rule
{
    return true;
}


template <class T>
vector<T> greedy()
{
    if (!C.empty && !is_solution(S))
    {
        x = select(C);
        pop(C, x);

        if (check(S, x))
        {
            add(S, x);
        }
    }
    return S;
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
    solution = greedy();
    cout << solution;
}


int main()
{
    input();
    init();
    solve();
    return 0;
}
