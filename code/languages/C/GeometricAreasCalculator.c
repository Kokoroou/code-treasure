#include<stdio.h>
#include<math.h>
#include<conio.h>

int main(){
	float p;
	float canh_hv, ban_kinh_ht, canh_tgd;
	
	printf("Nhap mot gia tri thuc: "); scanf("%f", &p);
	
	canh_hv = p/4;
	ban_kinh_ht = p/2/M_PI;
	canh_tgd = p/3;
	
	printf("Dien tich hinh vuong la: %.3f", canh_hv*canh_hv);
	printf("\nDien tich hinh tron la: %.3f", M_PI*ban_kinh_ht*ban_kinh_ht);
	printf("\nDien tich tam giac la: %.3f", sqrt(3)/4*canh_tgd*canh_tgd);
	
	getch();
	return 0;
}
