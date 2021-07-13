//https://open.kattis.com/problems/ratingproblems
#include <stdio.h>
//#include <string.h>
//#include <stdlib.h>

int main() {
	int n;
	scanf("%d", &n);
	int k;
	scanf("%d", &k);
	int sum = 0;
	
	for (int i = 0; i < k; i++)
	{
		int c;
		scanf("%d", &c);
		sum += c;
	}
	
	printf("%.4f %.4f", (sum+(n-k)*(-3.0))/n, (sum+(n-k)*(3.0))/n);
  return 0;
}
