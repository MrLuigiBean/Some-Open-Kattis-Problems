//https://open.kattis.com/problems/tarifa
#include <stdio.h>
//#include <string.h>
//#include <stdlib.h>

int main() {
	int x, n, temp;
	scanf("%d", &x);
	scanf("%d", &n);
	int sum = (n+1) * x;
	for (int i = 0; i < n; i++)
	{
		scanf("%d", &temp);
		sum -= temp;
	}
	printf("%d", sum);
  return 0;
}
