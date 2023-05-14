#include <stdio.h>
#include <stdlib.h>
void main(){
	int dataSize = sizeof(int) * 100;
	
	int *data = (int *)malloc(dataSize);
	free(&data[1]);
}
