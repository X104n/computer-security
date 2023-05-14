#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

void getFlag(){
	printf("Congrats! you can get the flag\n");
	fflush(stdout);
	system("cat flag");
}

int main(int argc, char **argv){
    struct {
        char buffer[16];
        volatile int (*funcPointer)();
    } stores;

    stores.funcPointer = NULL;

    printf("Try to get flag by inputing argument\n");
    fflush(stdout);

    assert(fgets(stores.buffer, 512, stdin) != NULL);

    if(stores.funcPointer){
        printf("Function is going to %p\n", stores.funcPointer);
        fflush(stdout);
        stores.funcPointer();
    }
    else{
        printf("oh no, please try again!\n");
    }

    return 0;
}
