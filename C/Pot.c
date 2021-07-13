//https://open.kattis.com/problems/pot
#include <stdio.h>
//#include <string.h>
//#include <stdlib.h>
#include <math.h>

int main() {
	int n;
	scanf("%d", &n);
	int sum = 0;
	for (int i = 0; i < n; i++)
	{
		int temp;
		scanf("%d", &temp);		
		sum += pow(temp / 10, temp % 10);
	}
	printf("%d", sum);
  return 0;
}
