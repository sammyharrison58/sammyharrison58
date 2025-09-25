#include <stdio.h>
int main(int argc, char** argv)
{
	int score=0 ;
	printf("enter the score/n:");
	scanf("%d", &score);
switch(score)
{
case 1 ... 40:printf("Grade D");
	break;
case 41 ... 60:printf("Grade C" );
	break;
case 61 ... 70:printf("Grade B");
	break;
case 71 ... 100:printf("Grade A");
	break;
default:printf("invalid/n");
	break;
}		
	return 0;
		
}