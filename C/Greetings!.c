//https://open.kattis.com/problems/greetings2
#include <stdio.h>
//#include <string.h>
//#include <stdlib.h>

int main() {
	char msg[1000];
	scanf("%s", msg);
	
	printf("%c", msg[0]);
	int e =  2 * (strlen(msg) - 2);
	for (int i=0; i< e; i++)
	{
		printf("%c", 'e');
	}
	printf("%c",msg[strlen(msg)-1]); 
  return 0;
}
