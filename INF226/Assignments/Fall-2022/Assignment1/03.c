#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>


void getFlag(){
    printf("Well done, you can get the flag\n");
    fflush(stdout);
    system("cat flag");
    return;
}

int main(int argc, char ** argv){

    unsigned long val = 5;
    struct { 
        char buffer[32];
        unsigned long* pt0;
    } locals;

    locals.pt0 = &val;

    while(locals.buffer[0] != 'q'){
        printf("Do not, for one repulse, forego the purpose that you resolved to effect -William Shakespeare, The Tempest\n");
        fflush(stdout);

        gets(locals.buffer);

        printf("%lx\n", *locals.pt0); 
      
        fflush(stdout);

    }

    return 0;
}
