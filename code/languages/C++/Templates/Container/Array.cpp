#include<bits/stdc++.h>
using namespace std;

int * func()
{
    // Return an array by its pointer
    int arr0[10];
    return arr0;
}

int main()
{
    // Declare
    int arr1[10];

    // Initialize
    int arr2[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int arr3[] = {1, 2, 3, 4, 5};
    int arr4[3][2] = {{1, 2}, {2, 3}, {3, 4}};

    // Access
    int var1 = arr2[3];
    int *var2 = arr2;
    int var3 = *(var2 + 3);

    return 0;
}
