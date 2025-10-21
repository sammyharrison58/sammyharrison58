#include<stdio.h>
int main()
{
	int choice;
	float area,radius,base,height,length,width,side;
	printf("area calculation");
	printf("enter your choice(1-2)");
	scanf("%d",&choice);
	
	switch(choice){
		case1:
		printf("enter the radius of the circle/n");
		scanf("%f",&radius);
		area=3.14*radius*radius;
		printf("area is :%f",area);
		break;
	case2:
	//triangle//
	printf("enter the base\n ");
	scanf("%f",&base);
	printf("enter the height");
	scanf("%f",&height);
	area=0.5*base*height;
	printf("area is :%f",area);
	break;
case3:
//rectangle//
printf("enter the length");
scanf("%f",&length);
printf("enter the height");
scanf("%f",&height);
area=length*width;
printf("area is:%f",area);
break;

	}
	return 0;
}