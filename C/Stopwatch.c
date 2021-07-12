//https://open.kattis.com/problems/stopwatch
#include <stdio.h>
//#include <string.h>
//#include <stdlib.h>

int main() {
	int size;
	scanf("%d", &size);

	if (size%2==1)
	{
		printf("still running");
	}

	else
	{
		int sum = 0;
		int t1, t2;
		for (int i = 0; i < size/2; i++)
		{
			scanf("%d", &t1);
			scanf("%d", &t2);
			sum += t2 - t1;
		}
		printf("%d", sum);
	}
  return 0;
}
