#include <stdio.h>
int main()
{
	int a, b;
	float total;
	printf("enter a/n");
	scanf("%d",&a);
	printf("enter b/n");
	scanf("%d",&b);
	total=a+b;
	printf("The sum of %d and %d is %f",a,b,total);
	return 0;
}
