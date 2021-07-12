//https://open.kattis.com/problems/electricaloutlets
//MASSIVE THANKS TO https://github.com/minidomo/Kattis/blob/master/C/electricaloutlets.c
#include <stdio.h>
//#include <string.h>
//#include <stdlib.h>

int main() {
	int n;
	scanf("%d", &n);
	while(n--)
	{
		int num;
		scanf("%d", &num);
		int ans;
		ans = 1 - num;
		while (num--)
		{
			int c;
			scanf("%d", &c);
			ans += c;
		}
		printf("%d\n", ans);
	}
  return 0;
}
