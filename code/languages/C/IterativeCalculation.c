#include<stdio.h>
#include<math.h>

int main(){
    float B = 4095.1;
    float A = B + 1;
    float x = 1;
    int n;
    printf("Khoi tao x = %.19f", x);
    for (n = 1; n <= 9; n++)
    {
        x = (A*x) - B;
        printf("\nLan thu thu %d x = %.19f", n, x);
    }

	return 1;
}
