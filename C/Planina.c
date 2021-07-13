//https://open.kattis.com/problems/planina
#include <stdio.h>
//#include <string.h>
//#include <stdlib.h>
#include <math.h>

int main() {
	int n;
	scanf("%d", &n);
	printf("%.0f", pow( pow(2, n) + 1, 2));
  return 0;
}
