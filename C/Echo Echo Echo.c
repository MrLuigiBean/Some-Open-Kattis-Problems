//https://open.kattis.com/problems/echoechoecho
#include <stdio.h>
//#include <string.h>
//#include <stdlib.h>

int main() {
	char text[15];
	scanf("%s", text);
	for (int i = 0; i < 3; i++)
	{
		printf("%s ", text);
	}
  return 0;
}
