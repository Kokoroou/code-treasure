#include<bits/stdc++.h>
using namespace std;

int main()
{
    // Declare
    stack<int> stack1;
    stack<int> stack2;

    // Add value
    stack1.push(19);  // Insert a copy of value
    stack2.emplace(19);  // Constructs a new element as the value then insert

    // Value at top
    int val1 = stack1.top();

    // Size of stack
    int val2 = stack1.size();

    // Pop value at top
    stack1.pop();

    // Check empty
    bool val3 = stack1.empty();

    // Swap 2 stack with same type
    stack1.swap(stack2);


}
