//https://open.kattis.com/problems/twostones
#include <stdio.h>
//#include <string.h>
//#include <stdlib.h>

int main() {
	int n;
	scanf("%d", &n);
	n % 2 == 1 ? printf("Alice") : printf("Bob");
  return 0;
}
