#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv){
    struct {
        char buffer[16];
        int32_t check;
    } locals;

    locals.check = 0xabcdc3cf;
    printf("Input an argument to pass\n");
    fflush(stdout);

    assert(fgets(locals.buffer, 512, stdin) != NULL);

    if(locals.check == 0x79beef8b) {
        printf("Well done, you can get the flag\n");
        fflush(stdout);
        system("cat flag");
    }
    else {
        printf("Uh oh, value is not correct. please try again. Goodbye.\n");
    }

    return 0;
}
