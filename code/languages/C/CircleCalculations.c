#include <stdio.h>
#include <math.h>
int main() {
	float r;
	printf("Nhap vao ban kinh duong tron: "); scanf("%f", &r);
	printf("Dien tich hinh tron la: %.3f", M_PI*r*r);
	printf("\nChu vi duong tron la: %.3f", 2*M_PI*r);
	
	return 0;
}
