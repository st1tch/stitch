#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, const char *argv[]) {

    if ((argc < 2) || strcmp(argv[1], "this_is_a_test")) {
        exit(1);
    }

    printf("win.\n");
    return 0;
}
