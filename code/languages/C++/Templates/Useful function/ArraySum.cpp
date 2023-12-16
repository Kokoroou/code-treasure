#include<bits/stdc++.h>
using namespace std;

int sum(int arr[], int len)
{
    int s = 0;  // Sum of array

    for (int i = 0; i < len; i++)
    {
        s += arr[i];
    }

    return s;
}
