#include <stdio.h>
#include <conio.h>

int main(){
	float const PI = 3.14159265;
	float r, S, P;
	printf("Ban kinh hinh tron la: ");
	scanf("%f", &r);
	if (r > 0){
		S=PI*r*r;
		P=2*PI*r;
		printf("Dien tich hinh tron la: %0.3f\n",S);
		printf("Chu vi hinh tron la: %0.3f\n",P);
	}
	else if (r <= 0){
		printf("Khong co hinh tron co ban kinh be hon hoac bang 0.\n");
	}
	getch();
	return 0;
}
