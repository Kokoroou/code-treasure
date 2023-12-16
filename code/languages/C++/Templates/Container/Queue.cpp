#include<bits/stdc++.h>
using namespace std;

int main()
{
    // Declare
    queue<int> queue1;
    queue<int> queue2;

    // Add value
    queue1.push(19);  // Insert a copy of value
    queue2.emplace(19);  // Constructs a new element as the value then insert

    // First and last value of queue
    int val1 = queue1.front();
    int val4 = queue1.back();

    // Size of queue
    int val2 = queue1.size();

    // Pop first value
    queue1.pop();

    // Check empty
    bool val3 = queue1.empty();

    // Swap 2 queue with same type
    queue1.swap(queue2);


}
