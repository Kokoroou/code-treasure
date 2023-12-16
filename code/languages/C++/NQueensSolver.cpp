#include<bits/stdc++.h>
#define N 100
using namespace std;

int n;
int x[N];

bool check(int v, int k)
{
    // return true if value v can be assigned to x[k] without violating condition
    return true;
}

void solution()
{
    for (int i = 0; i < n; i++)
        cout << x[i] << endl;
}

void Try(int k)
{
    // try all values for x[k], aware of x[1], x[2], ..., x[k-1]
    for (int v = 0; v < n; v++)
    {
        if (check(v, k))
        {
            x[k] = v;
            Try(k + 1);

        }
    }
}

int main()
{
    n = 4;
    Try(0);
}
