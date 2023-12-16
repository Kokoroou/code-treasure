#include <stdio.h>
#include <conio.h>

main(){
	int n, i, r, S=0;
	printf ("Cho so nguyen duong n (n<=1000) la:");
	scanf ("%d", &n);
	if (n > 0 && n <= 1000){
		for (i=1; i<=n; i++){
			r = n % i;
			if (r==0){
				S += i;
			}
		}
		printf ("Tong cac uoc nguyen duong cua n la: %d\n", S);
	}
	else {
		printf ("So khong hop le!\n");
	}
	getch();
	return 0;
}
