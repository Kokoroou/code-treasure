#include <stdio.h>
#include <conio.h>
#include <math.h>

main(){
	int N, i, b, c, x=0 ;
	int A[100];
	printf ("*Luu y: Chi nhap so nguyen duong.\n\n");
	printf ("So cac so nguyen cua day can tim la: ");
	scanf ("%d", &N);   
	if ((N>0) && (N<=100)){
		for (i=1; i<=N; i++){
			printf("So thu %d la ",i);
			scanf("%d", &A[i]);
			c=1;
			if ((A[i]>1) && (A[i]<10000)){
				for (b=2; b<=int(sqrt(A[i])); b++){
					c = c* (A[i]%b);
				}
				if (c != 0) {x+=1;}
			}
			else if ((A[i]<1) || (A[i]>=10000)){printf ("   => So qua nho hoac qua lon! \n");									
			}
		}
		printf ("\n    =>Day da cho co %d so nguyen to.",x);
	}
	else { printf ("   => Gia tri cho N qua lon hoac khong hop le! \n");
	}
	getch();  //Dung man hinh de xem
	return 0;
}
