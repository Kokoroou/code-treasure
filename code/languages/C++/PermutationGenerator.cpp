#include<bits/stdc++.h>
using namespace std;
#define N 20

// Variables definition
int x[N];  // Store solution
int n;  // Last index
bool visited[N];


void print_solution()
{
    for (int i = 1; i <= n; i++)
        cout << x[i] << " ";
    cout << endl;
}

bool check(int v, int k)
{
    return visited[v] == false;
}

void Try(int k)  // Try value for index k
{
    for (int v = 1; v <= n; v++)
    {
        if (check(v, k))
        {
            x[k] = v;  // Update value v for index k
            visited[v] = 1;

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
            visited[v] = 0;
        }
    }

}

void input()
{
    // Get value from input
    cin >> n;
}

void init()
{
    for (int v = 1; v <= n; v++)
        visited[v] = false;
}

void solve()
{
    // Solve problem
    Try(1);
}


int main()
{
    input();
    init();
    solve();
    return 0;
}
