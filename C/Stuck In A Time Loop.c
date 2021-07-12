//https://open.kattis.com/problems/timeloop
#include <stdio.h>
//#include <string.h>
//#include <stdlib.h>

int main() {
	int n;
	scanf("%d", &n);
	for (int i = 1; i < n+1; i++)
	{
		printf("%d Abracadabra\n", i);
	}
  return 0;
}
