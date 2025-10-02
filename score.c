#include <stdio.h>
int main()
{
	int score;
	printf("enter the score/n:");
	scanf("%d",&score);
	if (score <40)
		printf("Grade: E");
	else if (score<50)
	   	printf("Grade: D");
    else if (score<60)
	   	printf("Grade: C");
    else if (score<70)
	   	printf("Grade: B");
    else if (score<=100)
	   	printf("Grade: A");
    else
		printf("invalid");
	
	return 0;
}