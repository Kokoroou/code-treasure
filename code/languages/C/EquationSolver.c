#include<stdio.h>

int main(){
	float a, b, x;
	printf("Nhap a, b: "); scanf("%f %f", &a, &b);
	
	if (a<b) x = (a+b)/3;
	else if (a==b) x = 1.5172;
	else x = (a-b)/(a*a+b*b);
	
	printf("y = %.3f", 15*x*x + x + 7.2);
	return 0;
}
