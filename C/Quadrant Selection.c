//https://open.kattis.com/problems/quadrant
#include <stdio.h>
//#include <string.h>
//#include <stdlib.h>

int main() {
	int x;
	scanf("%d", &x);
	int y;
	scanf("%d", &y);
	if (x > 0 && y > 0)
		printf("1");
	else if (x < 0 && y > 0)
		printf("2");
	else if (x > 0 && y < 0)
		printf("4");
	else if (x < 0 && y < 0)
		printf("3");
  return 0;
}
