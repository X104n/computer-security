#include <stdio.h>
#include <stdlib.h>
void main(){
	int *data = (int *)malloc(sizeof(int) * 100);
	free(data);
	printf("%d\n", data[0]);
}
