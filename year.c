#include <stdio.h>
int main(int argc, char** argv)
{
	int y = 0;
	printf("enter the year/n:");
	scanf("%d", &y);
	if (y == 1)
	{
		printf("Good");
	}
	else if (y == 2)
	{
		printf("Not so good");
	}
	else if (y == 3)
	{
		printf("Not so bad");
	}
	else if (y == 4)
	{
		printf("bad");
	}
	else
	{
		printf("invalid");
	}

	return 0;
}

