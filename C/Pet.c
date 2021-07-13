//https://open.kattis.com/problems/pet
#include <stdio.h>
//#include <string.h>
//#include <stdlib.h>
//#include <math.h>

int add(int a, int b, int c, int d);

int main() {
	int hisc, sc, pos = 0;
	for (int i = 0; i < 5; i++)
	{
		int p1, p2, p3, p4;
		scanf("%d", &p1);
		scanf("%d", &p2);
		scanf("%d", &p3);
		scanf("%d", &p4);
		sc = add(p1, p2, p3, p4);
		if (sc > hisc)
		{
			hisc = sc;
			pos = i + 1;
		}
	}
	printf("%d %d", pos, hisc);
  return 0;
}

int add(int a, int b, int c, int d)
{
	return a+b+c+d;
}
